


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


# Strategy for Dodging Columns as a means of providing additional conditioning.
class ColumnDodgeStrategy(Strategy.Strategy):
    
    
    # Initializes an instance of a segment of the strategy.
    def initSegment(self, tmpObj : SceneGenerator.SceneGenerator, strtTimeI : float, randx : float , startXA : float , columnIndex : int ) :

        split2 = tmpObj.referenceTimeSplit;

        strtTimeA = strtTimeI;

        if True :
            tobj = tmpObj.dodgeColumnsA[0 + columnIndex];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(startXA, tmpObj.dodgeColumnHeight, tmpObj.backDistBucket);
            tobj.endPos.set(startXA, tmpObj.dodgeColumnHeight, 0);
            tobj.strtTime = strtTimeA;
            tobj.endTime = tobj.strtTime + 1.4 * tmpObj.flightTime;
            self.enableStart(tmpObj, tobj);
            self.randRotateFar(tmpObj, randx, tobj.strtPos);
            self.randRotateClose(tmpObj, randx, tobj.endPos);
            self.postAdjustEndpos(tmpObj, tobj.endPos);
        #if

        strtTimeA = strtTimeI + 2 * split2;
    
    
    # Initializes an instance of the strategy.
    def init(self, tmpObj : SceneGenerator.SceneGenerator , strtTimeI : float ) :

        split2 = tmpObj.referenceTimeSplit;
        randx = random.random();

        strtTimeA = strtTimeI;



        self.initSegment(tmpObj, strtTimeA, randx, 0.16, 0);


        tmpObj.endTime = strtTimeA + split2 + 1.4 * tmpObj.flightTime;
        

        tmpObj.dumbbellStrategy.initPotentialDisruptiveDumbbell(tmpObj, strtTimeI, tmpObj.endTime);


    # init
    

 
 
