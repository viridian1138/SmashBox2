


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


# Strategy for a front-ball kick to the leg from the left.  The targets show the target of the kick only.
class LeftFrontKickLegStrategy(Strategy.Strategy):
    
    # Initializes an instance of the strategy.
    def init(self, tmpObj : SceneGenerator.SceneGenerator , strtTimeI : float ) :

        split2 = tmpObj.referenceTimeSplit;
        randx = random.random();

        strtTimeA = strtTimeI;

        if True :
            startXA = -0.16;
            tobj = tmpObj.targetsKickB[0];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(startXA, tmpObj.offenseHeight * (tmpObj.legHeight / tmpObj.idealHumanHeadHeights ), tmpObj.backDistBucket);
            tobj.endPos.set(startXA, tmpObj.offenseHeight * (tmpObj.legHeight / tmpObj.idealHumanHeadHeights ), 0);
            tobj.strtTime = strtTimeA;
            tobj.endTime = tobj.strtTime + tmpObj.flightTimeKick;
            self.enableStart(tmpObj, tobj);
            self.randRotateFar(tmpObj, randx, tobj.strtPos);
            self.randRotateClose(tmpObj, randx, tobj.endPos);
            self.postAdjustEndpos(tmpObj, tobj.endPos);
        #if

        if True :
            startXA = -0.16;
            tobj = tmpObj.targetsKickB[1];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(startXA, tmpObj.offenseHeight * (tmpObj.legHeight / tmpObj.idealHumanHeadHeights ), tmpObj.backDistBucket);
            tobj.endPos.set(startXA, tmpObj.offenseHeight * (tmpObj.legHeight / tmpObj.idealHumanHeadHeights ), 0);
            tobj.strtTime = strtTimeA + split2;
            tobj.endTime = tobj.strtTime + tmpObj.flightTimeKick;
            self.enableStart(tmpObj, tobj);
            self.randRotateFar(tmpObj, randx, tobj.strtPos);
            self.randRotateClose(tmpObj, randx, tobj.endPos);
            self.postAdjustEndpos(tmpObj, tobj.endPos);
        # if

        if True :
            startXA = -0.16;
            tobj = tmpObj.targetsKickB[2];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(startXA, tmpObj.offenseHeight * (tmpObj.legHeight / tmpObj.idealHumanHeadHeights ), tmpObj.backDistBucket);
            tobj.endPos.set(startXA, tmpObj.offenseHeight * (tmpObj.legHeight / tmpObj.idealHumanHeadHeights ), 0);
            tobj.strtTime = strtTimeA + split2 + split2;
            tobj.endTime = tobj.strtTime + tmpObj.flightTimeKick;
            self.enableStart(tmpObj, tobj);
            self.randRotateFar(tmpObj, randx, tobj.strtPos);
            self.randRotateClose(tmpObj, randx, tobj.endPos);
            self.postAdjustEndpos(tmpObj, tobj.endPos);

            strtTimeA = tobj.endTime + self.xDeltaTime( tmpObj.flightTimeKick );
        # if

        tmpObj.endTime = strtTimeA;
        tmpObj.dumbbellStrategy.initPotentialDisruptiveDumbbell(tmpObj, strtTimeI, tmpObj.endTime);

    # init
    

 
 
