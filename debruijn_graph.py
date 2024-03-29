import numpy as np
import sys
from dna_sequence import CDNASequence
letters = ('A','C','G','T')
''' de Bruijn - graph representation '''
class CDeBruijnGraph(CDNASequence):
	''' implements a de Bruijn graph...'''
	def __init__(self,order):
		super(CDeBruijnGraph,self).__init__()
		self._order = order
		self._vertices = list() ## list of strings...
		self._edges = list(list())
		self._num_edges = 4**(self._order+1)
		self._num_vertices = int(self._num_edges/4)
		sys.setrecursionlimit(10**5)
		self.InitVertices(0,"")
		self.FastInitEdges()
	def __repr__(self):
		descr = "order: " + str(self._order) + " num_vertices: " + str(self._num_vertices)
		return(descr)
	def InitVertices(self,depth,curr_string):
		if(depth==self._order):
			self._vertices.append(curr_string)
		else:
			for i in range(0,4):
				self.InitVertices(depth+1,curr_string+letters[i])
	def FastInitEdges(self):
		curr_index=0
		for i in range(0,self._num_vertices):
			temp_list=list()
			for j in range(0,4):
				temp_list.append(curr_index+j)
			self._edges.append(temp_list)
			curr_index+=4
			if(curr_index>=self._num_vertices):
				curr_index=0
	def PrintVertices(self):
		print(self._vertices)
	def PrintEdges(self):
		print(self._edges)
	def GetNeighborsByVertexIndex(self,vertex_index):
		return self._edges[vertex_index]
	def GetNeighborsByVertexString(self,vertex_string):
		index_of_string = self.VertexIndexByName(vertex_string)
		return self.GetNeighborsByVertexIndex(index_of_string)
	def VertexNameByIndex(self,vertex_index):
		return self._vertices[vertex_index]
	def VertexIndexByName(self,vertex_string):
		return self._vertices.index(vertex_string)
	def GetNumberOfVertices(self):
		return self._num_vertices
	def GetNumberOfEdges(self):
		return self._num_edges
	def GetOrder(self):
		return self._order
	def DeleteEdge(self,first_index,second_index):
		## loop through the elements of the list self._edges[first_index]
		if(second_index in self._edges[first_index]):
			self._edges[first_index].remove(second_index)
	def DeleteEdgesByStrings(self,first_string,second_string):
		first_index = self.VertexIndexByName(first_string)
		second_index = self.VertexIndexByName(second_string)
		self.DeleteEdge(first_index,second_index)
		#for i in self._edges[first_index]:

	#def ShuffleEdgeIndicers(self,)
	
#cdbg = CDeBruijnGraph(6);
#print(cdbg)
#str=""
#cdbg.InitVertices(0,str)
#cdbg.FastInitEdges()
#cdbg.PrintEdges()
#indices = cdbg.GetNeighborsByVertexString("AACATG")
#print([cdbg.VertexNameByIndex(i) for i in indices])