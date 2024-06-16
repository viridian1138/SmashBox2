


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


# Strategy to occupy the right hand with a set of targets on the left before generating a dumbbell or hurdle.
class RightOccupyStrategy(Strategy.Strategy):
    
    # Initializes an instance of the strategy.
    def init(self, tmpObj : SceneGenerator.SceneGenerator , strtTimeI : float ) :

        split2 = tmpObj.referenceTimeSplit;
        randx = 0.1;

        strtTimeA = strtTimeI;

        stime = tmpObj.rightHookHeadStrategy.initSegment(tmpObj, strtTimeA, randx, 0);
        strtTimeA = stime + self.xDeltaTime( tmpObj.flightTime );





        if random.random() < 0.666 : 
            tmpObj.dumbbellStrategy.initIntervalDisruptiveDumbbell(tmpObj, tmpObj.targetsPunchA[0].strtTime, tmpObj.targetsPunchA[2].endTime, 0);
        else : 
            rand = random.random();
            startXA = 0;
            startXA = tmpObj.bucketXOffset;
            tobj = tmpObj.jumpHurdlesA[0];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(startXA, tmpObj.jumpHurdleHeight, tmpObj.backDistBucket);
            tobj.endPos.set(0, tmpObj.jumpHurdleHeight, 0);
            tobj.strtTime = strtTimeA;
            tobj.endTime = tobj.strtTime + tmpObj.flightTime;
            self.postAdjustEndpos(tmpObj, tobj.endPos);
            self.enableStart(tmpObj, tobj);

            strtTimeA = tobj.endTime + self.xDeltaTime( tmpObj.flightTime );
        # if



        tmpObj.endTime = strtTimeA;
        tmpObj.dumbbellStrategy.initPotentialDisruptiveDumbbell(tmpObj, strtTimeI, tmpObj.endTime);

    # init
    

 
 
