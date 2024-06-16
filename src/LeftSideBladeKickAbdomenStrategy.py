


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


# Strategy for a left side-blade kick to the abdomen.
class LeftSideBladeKickAbdomenStrategy(Strategy.Strategy):
    
    
    # Initializes an instance of a segment of the strategy.
    def initSegment(self, tmpObj : SceneGenerator.SceneGenerator, strtTimeI : float, tdelay : float , cameraPos : Vec3.Vec3 , kickIndex : int ) :

        strtTimeA = strtTimeI;
        split2 = tmpObj.referenceTimeSplit;


        if True :
            tobj = tmpObj.targetsKickB[ kickIndex+0 ];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(-abs(tmpObj.backDistBucket), tmpObj.offenseHeight * (tmpObj.abdomenHeight / tmpObj.idealHumanHeadHeights ), cameraPos.z);
            tobj.endPos.set(cameraPos.x, tmpObj.offenseHeight * (tmpObj.abdomenHeight / tmpObj.idealHumanHeadHeights ), cameraPos.z);
            tobj.strtTime = strtTimeA + tdelay;
            tobj.endTime = tobj.strtTime + tmpObj.flightTimeKick;
            self.enableStart(tmpObj, tobj);
        #if

        if True :
            tobj = tmpObj.targetsKickA[ kickIndex+0 ];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(-tmpObj.bucketXOffset, tmpObj.offenseHeight * (tmpObj.abdomenHeight / tmpObj.idealHumanHeadHeights ), tmpObj.backDistBucket);
            tobj.endPos.set(-abs(tmpObj.backDistBucket), tmpObj.offenseHeight * (tmpObj.abdomenHeight / tmpObj.idealHumanHeadHeights ), cameraPos.z);
            tobj.strtTime = strtTimeA;
            tobj.endTime = tobj.strtTime + tmpObj.flightTimeKick;
            self.enableStart(tmpObj, tobj);
        # if

        if True :
            tobj = tmpObj.targetsKickB[ kickIndex+1 ];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(-abs(tmpObj.backDistBucket), tmpObj.offenseHeight * (tmpObj.abdomenHeight / tmpObj.idealHumanHeadHeights ), cameraPos.z);
            tobj.endPos.set(cameraPos.x, tmpObj.offenseHeight * (tmpObj.abdomenHeight / tmpObj.idealHumanHeadHeights ), cameraPos.z);
            tobj.strtTime = strtTimeA + split2 + tdelay;
            tobj.endTime = tobj.strtTime + tmpObj.flightTimeKick;
            self.enableStart(tmpObj, tobj);
        # if
        
        if True :
            tobj = tmpObj.targetsKickA[ kickIndex+1 ];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(-tmpObj.bucketXOffset, tmpObj.offenseHeight * (tmpObj.abdomenHeight / tmpObj.idealHumanHeadHeights ), tmpObj.backDistBucket);
            tobj.endPos.set(-abs(tmpObj.backDistBucket), tmpObj.offenseHeight * (tmpObj.abdomenHeight / tmpObj.idealHumanHeadHeights ), cameraPos.z);
            tobj.strtTime = strtTimeA + split2;
            tobj.endTime = tobj.strtTime + tmpObj.flightTimeKick;
            self.enableStart(tmpObj, tobj);
        #if
         
        if True :
            tobj = tmpObj.targetsKickB[ kickIndex+2 ];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(-abs(tmpObj.backDistBucket), tmpObj.offenseHeight * (tmpObj.abdomenHeight / tmpObj.idealHumanHeadHeights ), cameraPos.z);
            tobj.endPos.set(cameraPos.x, tmpObj.offenseHeight * (tmpObj.abdomenHeight / tmpObj.idealHumanHeadHeights ), cameraPos.z);
            tobj.strtTime = strtTimeA + split2 + split2 + tdelay;
            tobj.endTime = tobj.strtTime + tmpObj.flightTimeKick;
            self.enableStart(tmpObj, tobj);
        #if
         
        if True :
            tobj = tmpObj.targetsKickA[ kickIndex+2 ];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(-tmpObj.bucketXOffset, tmpObj.offenseHeight * (tmpObj.abdomenHeight / tmpObj.idealHumanHeadHeights ), tmpObj.backDistBucket);
            tobj.endPos.set(-abs(tmpObj.backDistBucket), tmpObj.offenseHeight * (tmpObj.abdomenHeight / tmpObj.idealHumanHeadHeights ), cameraPos.z);
            tobj.strtTime = strtTimeA + split2 + split2;
            tobj.endTime = tobj.strtTime + tmpObj.flightTimeKick;
            self.enableStart(tmpObj, tobj);
            strtTimeA = tobj.strtTime;
        # if
                      
        return( strtTimeA );
    
    
    # Initializes an instance of the strategy.
    def init(self, tmpObj : SceneGenerator.SceneGenerator , strtTimeI : float ) :

        split2 = tmpObj.referenceTimeSplit;
        cameraPos = tmpObj.hmdLocn
        tdelay = 2 * split2;

        strtTimeA = strtTimeI;

        jumping = random.random() < 0.25;

        # Potentially modifies to a jumping kick.
        if jumping :
            tobj = tmpObj.jumpHurdlesA[0];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(-abs(tmpObj.backDistBucket), tmpObj.jumpHurdleHeight, cameraPos.z);
            tobj.endPos.set(cameraPos.x, tmpObj.jumpHurdleHeight, cameraPos.z);
            tobj.strtTime = strtTimeA + tdelay;
            tobj.endTime = tobj.strtTime + tmpObj.flightTimeKick;
            self.enableStart(tmpObj, tobj);
        # if

        if jumping :
            tobj = tmpObj.jumpHurdlesA[2];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(-tmpObj.bucketXOffset, tmpObj.jumpHurdleHeight, tmpObj.backDistBucket);
            tobj.endPos.set(cameraPos.x, tmpObj.jumpHurdleHeight, cameraPos.z);
            tobj.strtTime = strtTimeA;
            tobj.endTime = tobj.strtTime + tdelay + tmpObj.flightTimeKick;
            self.enableStart(tmpObj, tobj);
        # if

        if jumping :
            tobj = tmpObj.jumpHurdlesA[1];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(-tmpObj.bucketXOffset, tmpObj.jumpHurdleHeight, tmpObj.backDistBucket);
            tobj.endPos.set(-abs(tmpObj.backDistBucket), tmpObj.jumpHurdleHeight, cameraPos.z);
            tobj.strtTime = strtTimeA;
            tobj.endTime = tobj.strtTime + tmpObj.flightTimeKick;
            self.enableStart(tmpObj, tobj);
            strtTimeA = strtTimeA + tmpObj.jumpingKickDelay;
        # if

        # ----------------------------------------


        strtTimeA = self.initSegment(tmpObj, strtTimeA, tdelay, cameraPos, 0);
        strtTimeA = strtTimeA + tdelay + tmpObj.flightTimeKick + self.xDeltaTime( tmpObj.flightTimeKick );


        tmpObj.endTime = strtTimeA;
        tmpObj.dumbbellStrategy.initPotentialDisruptiveDumbbell(tmpObj, strtTimeI, tmpObj.endTime);

    # init
    

 
 
