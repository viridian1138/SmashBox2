


#$$strtCprt
"""
* Smash Box 2 (Full Body Track) VR
* 
* Copyright (C) 2022-2024 Thornton Green
* 
* This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as
* published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
* This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty 
* of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
* You should have received a copy of the GNU General Public License along with this program; if not, 
* see <http://www.gnu.org/licenses>.
* Additional permission under GNU GPL version 3 section 7
*
"""
#$$endCprt



import Vec3
import Face3


class RetainedMode(object):
    
    def __init__(self):
        self.vertices = []
        self.faces = []
        self.indices = []
        self.storedVertexLength = 0
        
    def allocVertex(self):
        vec3 = Vec3.Vec3()
        self.vertices = self.vertices + [ vec3 ]
        return vec3 
        
    def allocFace(self):
        face3 = Face3.Face3()
        self.faces = self.faces + [ face3 ]
        return face3
        
    def storeVertexLength(self):
        self.storedVertexLength = len( self.vertices )
        
    def allocIndices(self, indexList : list ) :
        storedVertexLength = self.storedVertexLength
        prevIndexLength = len( self.indices ) 
        self.indices = self.indices + indexList;
        for cnt in range( prevIndexLength , len( self.indices ) ) :
            self.indices[ cnt ] = self.indices[ cnt ] + storedVertexLength
        
    def uniformLayoutStr(self):
        currentUniformIndex = 100
        sz = str(len(self.vertices))
        ret = "\n"
        for x in range(len(self.vertices)):
            if not ( self.vertices[x].getFixedPosn() ) :
                indexStr = str( currentUniformIndex )
                ret = ret + "layout(location = " + indexStr + ") uniform vec3 uniformVector" + indexStr + "; \n"
                self.vertices[x].setUniformIndex( currentUniformIndex )
                currentUniformIndex = currentUniformIndex + 3
        ret = ret + "\n"
        self.numUniforms = currentUniformIndex - 100
        return ret
        
    def vertexStr(self):
        sz = str(len(self.vertices))
        ret = "const vec3 VERTEX_ARR[" + sz + "] = vec3[" + sz + "]( \n"
        for x in range(len(self.vertices)):
            ret = ret + self.vertices[x].retainedStr()
            if not x == ( len(self.vertices) - 1 ) :
                ret = ret + ","
            ret = ret + "\n"
        ret = ret + "            ); \n"
        return ret
        
    def faceColorStr(self):
        sz = str(len(self.faces))
        ret = "const vec3 FACE_COLORS[" + sz + "] = vec3[" + sz + "]( \n"
        for x in range(len(self.faces)):
            ret = ret + self.faces[x].faceColor.retainedStr()
            if not x == ( len(self.faces) - 1 ) :
                ret = ret + ","
            ret = ret + "\n"
        ret = ret + "            ); \n"
        return ret
        
    def faceUnitNormalStr(self):
        sz = str(len(self.faces))
        ret = "const vec3 FACE_UNIT_NORMALS[" + sz + "] = vec3[" + sz + "]( \n"
        for x in range(len(self.faces)):
            ret = ret + self.faces[x].normal.retainedStr()
            if not x == ( len(self.faces) - 1 ) :
                ret = ret + ","
            ret = ret + "\n"
        ret = ret + "            ); \n"
        return ret
        
    def faceIndexStr1(self):
        ret = ""
        
        if len( self.indices ) > ( 999 * 4 - 1 ) :
           raise Exception( "Internal Error" )
        
        if True :
            szI = ( 999 * 2 )
            sz = str(szI)
            ret = ret + "const int FACE_INDICES[" + sz + "] = int[" + sz + "]( \n"
            for x in range(szI):
                r = self.indices[x]
                ret = ret + str( r )
                if not x == ( szI - 1 ) :
                    ret = ret + ","
                ret = ret + "\n"
            ret = ret + "            ); \n"
        
        return ret
        
    def faceIndexStr2(self):
        ret = ""
        
        if len( self.indices ) > ( 999 * 4 - 1 ) :
           raise Exception( "Internal Error" )
        
        ret = ret + "\n"
        
        if True :
            szI = len(self.indices) - ( 999 * 2 )
            sz = str(szI)
            ret = ret + "const int FACE_INDICES[" + sz + "] = int[" + sz + "]( \n"
            for x in range(szI):
                r = self.indices[x+( 999 * 2 )]
                ret = ret + str( r )
                if not x == ( szI - 1 ) :
                    ret = ret + ","
                ret = ret + "\n"
            ret = ret + "            ); \n"
        
        return ret
    
    def getIndexSize1(self):
        return ( 999 * 2 )
    
    def getIndexSize2(self):
        return len(self.indices) - ( 999 * 2 )
        
    
  
   
  
    