from debruijn_graph import CDeBruijnGraph
from dna_sequence import CDNASequence
from dna_sequence import DNASequRevComplement
import numpy as np
import datetime
import random

class CDeBruijnSequence(CDNASequence):
	def __init__(self,order_sequ=7,is_circular=False,rev_comp_free=False,initial_sequence="",length=7560):
		CDNASequence.__init__(self)
		self._order_of_sequ = order_sequ
		self._db_graph = CDeBruijnGraph(order_sequ-1) ## order of the underlying De Bruijn-Graph is smaller by 1 than the order of the De Bruijn sequence
		self._is_circular = is_circular
		self._rev_comp_free = rev_comp_free
		self._initial_sequence = initial_sequence
		self._scaffold_length = length

		self._solution_found = False
		self._end_reached = False

		self._initial_depth=0
		self._timedelta_max = datetime.timedelta(0,2,0) ## a maximum of 3 s

	def CreateDeBruijnSequence(self):
		## start with random index:
		num_vertices = self._db_graph.GetNumberOfVertices()
		cti = np.random.randint(0,num_vertices)
		
		if(self._initial_sequence==""):
			print("initial sequence is empty")
			self._initial_tuple_index = cti
			self._initial_depth=0
		elif(self._initial_sequence!=""):
			print("initial sequence is not empty")
			first_tuple_string = self._initial_sequence[0:self._db_graph.GetOrder()]
			self._initial_tuple_index=self._db_graph.VertexIndexByName(first_tuple_string)
			self._sequ=self._initial_sequence[0:len(self._initial_sequence)-self._db_graph.GetOrder()]
			self._sequ_last_tuple = self._initial_sequence[len(self._initial_sequence)-self._db_graph.GetOrder():len(self._initial_sequence)]
			cti = self._db_graph.VertexIndexByName(self._sequ_last_tuple)
			self._initial_depth=len(self._sequ)
		self._starting_time = datetime.datetime.now()
		self._ConsiderInitialSequence()
		self._CreateDeBruijnSequenceRecursively(self._sequ,cti,self._initial_depth,self._rev_comp_free)
	def _ConsiderInitialSequence(self):
		if(self._initial_sequence!=""):
			print("considering initial sequence:")
			subsequences = list()
			str_length = len(self._initial_sequence)
			for i in range(0,(str_length-self._db_graph.GetOrder())):
				subsequences.append(self._initial_sequence[i:i+self._db_graph.GetOrder()+1])
			print(subsequences)
	def _CreateDeBruijnSequenceRecursively(self,curr_sequ,curr_tuple_index,curr_depth,rev_comp_free):
		self._curr_time = datetime.datetime.now()
		#print(curr_depth)
		if((self._curr_time-self._starting_time)>self._timedelta_max):
			print("TIME OUT")
			self._end_reached=True
			self._solution_found=False
			return
		if(curr_depth==self._scaffold_length):
			print("final depth reached")
			print("time required: ")
			dt = self._curr_time-self._starting_time
			print(dt)
			self._sequ=curr_sequ
			self._end_reached=True
			if(self._is_circular==True):
				if(curr_tuple_index==self._initial_tuple_index):
					print("circular solution found")
					self._solution_found=True
				else:
					print("no circular solution found")
					self._solution_found=False
			else:
				print("linear solution found")
				self._solution_found=True
			return
		else:	## final length not yet reached
			if(self._end_reached==False): ## check whether time-out has occured 
				self._sequ+=self._db_graph.VertexNameByIndex(curr_tuple_index)[0]
				curr_neighbors = self._db_graph.GetNeighborsByVertexIndex(curr_tuple_index)
				num_neighbors = len(curr_neighbors)
				random.shuffle(curr_neighbors)
				#curr_neighbors2 = self._db_graph.GetNeighborsByVertexIndex(curr_tuple_index)
				for i in range(0,num_neighbors):
					first_element = curr_neighbors[0]
					#print(first_element)
					index_rev_comp_first=0
					index_rev_comp_second=0
					contained_tuple=False
					if(rev_comp_free==True):
						pass
					curr_neighbors.remove(first_element)


					self._CreateDeBruijnSequenceRecursively(self._sequ,first_element,curr_depth+1,rev_comp_free)
					curr_neighbors.append(first_element)
					#curr_neighbors.append(index_rev_comp_second)

						#first_letter = self._db_graph.VertexNameByIndex(curr_tuple_index)[0]
						#first_letter = self._db_graph.VertexNameByIndex(curr_tuple_index)[0]
						#print("order of DB-sequence:")
						#print(self._db_graph.GetOrder())
						#print("number of vertices:")
						#print(self._db_graph.GetNumberOfVertices())
						#print(first_element)
						#rest_of_sequ = self._db_graph.VertexNameByIndex(first_element)

						#print(first_letter)
						#print(rest_of_sequ)
						## tuple-sequence that would be created by going to the current tuple candidate...:
						#print(self._db_graph.VertexNameByIndex(curr_tuple_index)[0])
						#print(self._db_graph.VertexNameByIndex(first_element)[0:self._db_graph.GetOrder()])
						#curr_tup_sequence=self._db_graph.VertexNameByIndex(curr_tuple_index)[0] + self._db_graph.VertexNameByIndex(first_element)[0:self._db_graph.GetOrder()]
#
#						curr_rev_comp_sequence = DNASequRevComplement(curr_tup_sequence)
						#print(curr_tup_sequence)
						#print(curr_rev_comp_sequence)
#						index_rev_comp_first=self._db_graph.VertexIndexByName(curr_rev_comp_sequence[0:self._db_graph.GetOrder()])
#						index_rev_comp_second=self._db_graph.VertexIndexByName(curr_rev_comp_sequence[1:self._db_graph.GetOrder()+1])
#						curr_nbs_rc = self._db_graph.GetNeighborsByVertexIndex(index_rev_comp_first)
#						contained_tuple = index_rev_comp_second in curr_nbs_rc
#						if((curr_tup_sequence==curr_rev_comp_sequence) and (contained_tuple==True)):
#							curr_nbs_rc.remove(index_rev_comp_second)
##							curr_nbs_rc.append(index_rev_comp_second)#
							#continu#e
						#if(contained_tuple==True):
					#		curr_nbs_rc.remove(index_rev_comp_second)
				#	del curr_nbs_rc[0]
				#	self._CreateDeBruijnSequenceRecursively(curr_sequ,first_element,curr_depth+1,rev_comp_free)
				#	curr_neighbors.append(first_element)
				###	if(rev_comp_free==True):
				#		curr_nbs_rc = self._db_graph.GetNeighborsByVertexIndex(index_rev_comp_first)
				#		if(((index_rev_comp_second in curr_nbs_rc)==False) and (contained_tuple==True)):
				#			curr_nbs_rc.append(index_rev_comp_second)
			#else:
			#	return
					#GetReverseComplement(self)
dbs = CDeBruijnSequence(7,initial_sequence="ACTCAGCACGGTGTTTAAAC",length=7560,rev_comp_free=True)
dbs.CreateDeBruijnSequence()
dbstr = dbs.GetSequence()
print("string:")
print(dbstr)