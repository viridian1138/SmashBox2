


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


# Strategy for generating some random jump hurdles.
class JumpHurdleStrategy(Strategy.Strategy):
    
    # Initializes an instance of the strategy.
    def init(self, tmpObj : SceneGenerator.SceneGenerator , strtTimeI : float ) :

        split2 = tmpObj.referenceTimeSplit;

        strtTimeA = strtTimeI;
        strtTimeB = strtTimeI;

        if True :
            rand = random.random();
            startXA = 0;
            if rand < 0.3333 : 
                startXA = -tmpObj.bucketXOffset;
            if rand > 0.6666 :
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
        #if

        if random.random() < 0.2 :
            rand = random.random();
            startXA = 0;
            if rand < 0.3333 : 
                startXA = -tmpObj.bucketXOffset;
            if rand > 0.6666 : 
                startXA = tmpObj.bucketXOffset;
            tobj = tmpObj.jumpHurdlesA[1];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(startXA, tmpObj.jumpHurdleHeight, tmpObj.backDistBucket);
            tobj.endPos.set(0, tmpObj.jumpHurdleHeight, 0);
            tobj.strtTime = strtTimeB + split2 + split2;
            tobj.endTime = tobj.strtTime + tmpObj.flightTime;
            self.postAdjustEndpos(tmpObj, tobj.endPos);
            self.enableStart(tmpObj, tobj);

            strtTimeB = tobj.endTime + self.xDeltaTime( tmpObj.flightTime );
        # if

        tmpObj.endTime = strtTimeA;
        if strtTimeB > strtTimeA :
            tmpObj.endTime = strtTimeB;
        # if

    # init
    

 
 
