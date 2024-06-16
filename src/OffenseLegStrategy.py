


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



import random

import Strategy
import SceneGenerator
import Vec3


# Strategy for moves in which the player is on offense.
class OffenseLegStrategy(Strategy.Strategy):
    
    
    # Initializes an instance of the strategy.
    def init(self, tmpObj : SceneGenerator.SceneGenerator , strtTimeI : float ) :

        randx = random.random();

        if randx <= 0.3333333 :
            randn = random.randrange( len( tmpObj.strategiesOffenseLegRight ) )

            return tmpObj.strategiesOffenseLegRight[randn].init(tmpObj, strtTimeI);
        # if

        if randx <= 0.66666666 :
            randn = random.randrange( len( tmpObj.strategiesOffenseLegLeft ) )

            return tmpObj.strategiesOffenseLegLeft[randn].init(tmpObj, strtTimeI);
        # if


        randn = random.randrange( len( tmpObj.strategiesOffenseLegMid ) )

        return tmpObj.strategiesOffenseLegMid[randn].init(tmpObj, strtTimeI);


    # init
    

 
 
