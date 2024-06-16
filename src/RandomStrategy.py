


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


# Strategy for generating a random set of targets to block.
class RandomStrategy(Strategy.Strategy):
    
    # Initializes an instance of the strategy.
    def init(self, tmpObj : SceneGenerator.SceneGenerator , strtTimeI : float ) :

        split2 = tmpObj.randomStrategyTimeSplit;

        strtTimeA = strtTimeI;
        strtTimeB = strtTimeI + split2;

        if True :
            height = (0.5 + random.random() / 2) * (tmpObj.defenseHeight);
            startXA = 0.0 if random.random() < 0.5 else tmpObj.bucketXOffset;
            tobj = tmpObj.targetsPunchA[0];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(startXA, height, tmpObj.backDistBucket);
            tobj.endPos.set(0, height, 0);
            tobj.strtTime = strtTimeA;
            tobj.endTime = tobj.strtTime + tmpObj.flightTimeStraightPunch;
            self.postAdjustEndpos(tmpObj, tobj.endPos);
            self.enableStart(tmpObj, tobj);

            strtTimeA = tobj.endTime + self.xDeltaTime( tmpObj.flightTimeStraightPunch );
        #if

        if True :
            height = (0.5 + random.random() / 2) * (tmpObj.defenseHeight);
            startXB = 0.0 if random.random() < 0.5 else -tmpObj.bucketXOffset;
            tobj = tmpObj.targetsPunchB[0];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(startXB, height, tmpObj.backDistBucket);
            tobj.endPos.set(0, height, 0);
            tobj.strtTime = strtTimeB;
            tobj.endTime = tobj.strtTime + tmpObj.flightTimeStraightPunch;
            self.postAdjustEndpos(tmpObj, tobj.endPos);
            self.enableStart(tmpObj, tobj);

            strtTimeB = tobj.endTime + self.xDeltaTime( tmpObj.flightTimeStraightPunch );
        #if


        if True :
            height = (0.5 + random.random() / 2) * (tmpObj.defenseHeight);
            startXA = 0.0 if random.random() < 0.5 else tmpObj.bucketXOffset;
            tobj = tmpObj.targetsPunchA[1];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(startXA, height, tmpObj.backDistBucket);
            tobj.endPos.set(0, height, 0);
            tobj.strtTime = strtTimeA;
            tobj.endTime = tobj.strtTime + tmpObj.flightTimeStraightPunch;
            self.postAdjustEndpos(tmpObj, tobj.endPos);
            self.enableStart(tmpObj, tobj);

            strtTimeA = tobj.endTime + self.xDeltaTime( tmpObj.flightTimeStraightPunch );
        #if

        if True :
            height = (0.5 + random.random() / 2) * (tmpObj.defenseHeight);
            startXB = 0.0 if random.random() < 0.5 else -tmpObj.bucketXOffset;
            tobj = tmpObj.targetsPunchB[1];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(startXB, height, tmpObj.backDistBucket);
            tobj.endPos.set(0, height, 0);
            tobj.strtTime = strtTimeB;
            tobj.endTime = tobj.strtTime + tmpObj.flightTimeStraightPunch;
            self.postAdjustEndpos(tmpObj, tobj.endPos);
            self.enableStart(tmpObj, tobj);

            strtTimeB = tobj.endTime + self.xDeltaTime( tmpObj.flightTimeStraightPunch );
        #if

        if True :
            height = (0.5 + random.random() / 2) * (tmpObj.defenseHeight);
            startXA = 0.0 if random.random() < 0.5 else tmpObj.bucketXOffset;
            tobj = tmpObj.targetsPunchA[2];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(startXA, height, tmpObj.backDistBucket);
            tobj.endPos.set(0, height, 0);
            tobj.strtTime = strtTimeA;
            tobj.endTime = tobj.strtTime + tmpObj.flightTimeStraightPunch;
            self.postAdjustEndpos(tmpObj, tobj.endPos);
            self.enableStart(tmpObj, tobj);

            strtTimeA = tobj.endTime + self.xDeltaTime( tmpObj.flightTimeStraightPunch );
        #if

        if True :
            height = (0.5 + random.random() / 2) * (tmpObj.defenseHeight);
            startXB = 0.0 if random.random() < 0.5 else -tmpObj.bucketXOffset;
            tobj = tmpObj.targetsPunchB[2];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(startXB, height, tmpObj.backDistBucket);
            tobj.endPos.set(0, height, 0);
            tobj.strtTime = strtTimeB;
            tobj.endTime = tobj.strtTime + tmpObj.flightTimeStraightPunch;
            self.postAdjustEndpos(tmpObj, tobj.endPos);
            self.enableStart(tmpObj, tobj);

            strtTimeB = tobj.endTime + self.xDeltaTime( tmpObj.flightTimeStraightPunch );
        #if 


        tmpObj.endTime = strtTimeA;
        if strtTimeB > strtTimeA :
            tmpObj.endTime = strtTimeB;
        # if
        tmpObj.dumbbellStrategy.initPotentialDisruptiveDumbbell(tmpObj, strtTimeI, tmpObj.endTime);


    # init
    

 
 
