


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



import SceneGenerator
import Strategy

# A container for another set of strategies.
# NOTE: this is intended to be akin to an abstract class.  It has to be configured by another Strategy before use.
class ContainerStrategy(Strategy.Strategy) :
    
    def init(self, tmpObj : SceneGenerator.SceneGenerator , strtTimeI : float ):
        
        self.immediateSequence.init(tmpObj, strtTimeI);

        tmpObj.nextSequence = self.nextSequence;

 
 
