


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


# Strategy for a right uppercut jump.
class RightUppercutJumpStrategy(Strategy.Strategy):
    
    # Initializes an instance of the strategy.
    def init(self, tmpObj : SceneGenerator.SceneGenerator , strtTimeI : float ) :

        split2 = tmpObj.referenceTimeSplit;
        split3 = 0.75 * split2;
        randx = random.random();

        strtTimeA = strtTimeI;

        if True :
            tobj = tmpObj.jumpHurdlesA[0];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(0.0, tmpObj.jumpHurdleHeight, tmpObj.backDistBucket);
            tobj.endPos.set(0.0, tmpObj.jumpHurdleHeight, 0);
            tobj.strtTime = strtTimeA;
            tobj.endTime = tobj.strtTime + tmpObj.flightTime;
            self.enableStart(tmpObj, tobj);
            self.randRotateFar(tmpObj, randx, tobj.strtPos);
            self.randRotateClose(tmpObj, randx, tobj.endPos);
            self.postAdjustEndpos(tmpObj, tobj.endPos);
        #if

        if True :
            startXA = 0.08;
            tobj = tmpObj.targetsPunchA[0];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(startXA, tmpObj.offenseHeight * (tmpObj.uppercutJumpHeight / tmpObj.idealHumanHeadHeights ) - 2 * startXA, tmpObj.backDistBucket);
            tobj.endPos.set(startXA, tmpObj.offenseHeight * (tmpObj.uppercutJumpHeight / tmpObj.idealHumanHeadHeights ) - 2 * startXA, 0);
            tobj.strtTime = strtTimeA;
            tobj.endTime = tobj.strtTime + tmpObj.flightTime;
            self.enableStart(tmpObj, tobj);
            self.randRotateFar(tmpObj, randx, tobj.strtPos);
            self.randRotateClose(tmpObj, randx, tobj.endPos);
            self.postAdjustEndpos(tmpObj, tobj.endPos);
        # if

        if True :
            startXA = 0.0;
            tobj = tmpObj.targetsPunchA[1];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(startXA, tmpObj.offenseHeight * (tmpObj.uppercutJumpHeight / tmpObj.idealHumanHeadHeights ), tmpObj.backDistBucket);
            tobj.endPos.set(startXA, tmpObj.offenseHeight * (tmpObj.uppercutJumpHeight / tmpObj.idealHumanHeadHeights ), 0);
            tobj.strtTime = strtTimeA + split3;
            tobj.endTime = tobj.strtTime + tmpObj.flightTime;
            self.enableStart(tmpObj, tobj);
            self.randRotateFar(tmpObj, randx, tobj.strtPos);
            self.randRotateClose(tmpObj, randx, tobj.endPos);
            self.postAdjustEndpos(tmpObj, tobj.endPos);
        # if

        if True :
            startXA = -0.08;
            tobj = tmpObj.targetsPunchA[2];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(startXA, tmpObj.offenseHeight * (tmpObj.uppercutJumpHeight / tmpObj.idealHumanHeadHeights ) - 2 * startXA, tmpObj.backDistBucket);
            tobj.endPos.set(startXA, tmpObj.offenseHeight * (tmpObj.uppercutJumpHeight / tmpObj.idealHumanHeadHeights ) - 2 * startXA, 0);
            tobj.strtTime = strtTimeA + split3 + split3;
            tobj.endTime = tobj.strtTime + tmpObj.flightTime;
            self.enableStart(tmpObj, tobj);
            self.randRotateFar(tmpObj, randx, tobj.strtPos);
            self.randRotateClose(tmpObj, randx, tobj.endPos);
            self.postAdjustEndpos(tmpObj, tobj.endPos);

            strtTimeA = tobj.endTime + self.xDeltaTime( tmpObj.flightTime );
        # if

        tmpObj.endTime = strtTimeA;
        tmpObj.dumbbellStrategy.initPotentialDisruptiveDumbbell(tmpObj, strtTimeI, tmpObj.endTime);

    # init
    

 
 
