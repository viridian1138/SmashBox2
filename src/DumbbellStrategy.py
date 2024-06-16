


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


# Strategy for generating random dumbbels.
class DumbbellStrategy(Strategy.Strategy):
    
    # Initializes an instance of the strategy.
    def init(self, tmpObj : SceneGenerator.SceneGenerator , strtTimeI : float ) :

        split2 = tmpObj.referenceTimeSplit;

        strtTimeA = strtTimeI;
        strtTimeB = strtTimeI;

        if True :
            rand = random.random();
            startXA = 0;
            if rand < 0.3333 : startXA = -tmpObj.bucketXOffset;
            if rand > 0.6666 : startXA = tmpObj.bucketXOffset;
            tobj = tmpObj.dumbbelsA[0];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(startXA, tmpObj.defenseHeight * (tmpObj.dumbbellHeight / tmpObj.idealHumanHeadHeights ), tmpObj.backDistBucket);
            tobj.endPos.set(0, tmpObj.defenseHeight * (tmpObj.dumbbellHeight / tmpObj.idealHumanHeadHeights ), 0);
            if random.random() < 0.1 :
                insideI = abs(startXA) < 0.1;
                startYA = tmpObj.defenseHeight - 0.16 - 0.25 * tmpObj.backDistBucket if insideI else tmpObj.defenseHeight - 0.16 + 0.25 * tmpObj.bucketHypotenuse;
                tobj.strtPos.y = startYA;
            tobj.strtTime = strtTimeA;
            tobj.endTime = tobj.strtTime + tmpObj.flightTimeDumbbell;
            self.postAdjustEndpos(tmpObj, tobj.endPos);
            self.enableStart(tmpObj, tobj);

            strtTimeA = tobj.endTime + self.xDeltaTime( tmpObj.flightTimeDumbbell );
        # if



        if random.random() < 0.2 :
            rand = random.random();
            startXA = 0;
            if rand < 0.3333 : startXA = -tmpObj.bucketXOffset;
            if rand > 0.6666 : startXA = tmpObj.bucketXOffset;
            tobj = tmpObj.dumbbelsA[1];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(startXA, tmpObj.defenseHeight * (tmpObj.dumbbellHeight / tmpObj.idealHumanHeadHeights ), tmpObj.backDistBucket);
            tobj.endPos.set(0, tmpObj.defenseHeight * (tmpObj.dumbbellHeight / tmpObj.idealHumanHeadHeights ), 0);
            if random.random() < 0.1 :
                insideI = abs(startXA) < 0.1;
                startYA = tmpObj.defenseHeight - 0.16 - 0.25 * tmpObj.backDistBucket if insideI else tmpObj.defenseHeight - 0.16 + 0.25 * tmpObj.bucketHypotenuse;
                tobj.strtPos.y = startYA;
            tobj.strtTime = strtTimeB + split2 + split2;
            tobj.endTime = tobj.strtTime + tmpObj.flightTimeDumbbell;
            self.postAdjustEndpos(tmpObj, tobj.endPos);
            self.enableStart(tmpObj, tobj);

            strtTimeB = tobj.endTime + self.xDeltaTime( tmpObj.flightTimeDumbbell );
        # if



        tmpObj.endTime = strtTimeA;
        if strtTimeB > strtTimeA :
            tmpObj.endTime = strtTimeB;
        # if


    # init
    
    
    



    # Generates a disruptive dumbbell between the start time and the end time.
    def initPotentialDisruptiveDumbbell(self , tmpObj : SceneGenerator.SceneGenerator , strtTimeI : float , endTimeI : float ) :

        if ((random.random() < 0.1) and (((-0.05) + endTimeI - strtTimeI) > tmpObj.flightTimeDumbbell)) :
            iDelta = (endTimeI - strtTimeI) - tmpObj.flightTimeDumbbell;
            strtTimeA = strtTimeI + iDelta * (random.random());
            rand = random.random();
            startXA = 0;
            if rand < 0.3333 : startXA = -tmpObj.bucketXOffset;
            if rand > 0.6666 : startXA = tmpObj.bucketXOffset;
            tobj = tmpObj.dumbbelsA[tmpObj.maxDumbbels - 1];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(startXA, tmpObj.defenseHeight * (tmpObj.dumbbellHeight / tmpObj.idealHumanHeadHeights ), tmpObj.backDistBucket);
            tobj.endPos.set(0, tmpObj.defenseHeight * (tmpObj.dumbbellHeight / tmpObj.idealHumanHeadHeights ), 0);
            if random.random() < 0.1 : 
                insideI = abs(startXA) < 0.1;
                startYA = tmpObj.defenseHeight - 0.16 - 0.25 * tmpObj.backDistBucket if insideI else tmpObj.defenseHeight - 0.16 + 0.25 * tmpObj.bucketHypotenuse;
                tobj.strtPos.y = startYA;
            tobj.strtTime = strtTimeA;
            tobj.endTime = tobj.strtTime + tmpObj.flightTimeDumbbell;
            self.postAdjustEndpos(tmpObj, tobj.endPos);
            self.enableStart(tmpObj, tobj);

    # initPotentialDisruptiveDumbbell



    # Generates a disruptive dumbbell between the start time and the end time.
    def initIntervalDisruptiveDumbbell(self, tmpObj : SceneGenerator.SceneGenerator , strtTimeI : float , endTimeI : float , dumbbellIndex : int ) :

        if (((-0.05) + endTimeI - strtTimeI) > tmpObj.flightTimeDumbbell) :
            iDelta = (endTimeI - strtTimeI) - tmpObj.flightTimeDumbbell;
            strtTimeA = strtTimeI + iDelta * (random.random());
            rand = random.random();
            startXA = 0;
            if rand < 0.3333 : startXA = -tmpObj.bucketXOffset;
            if rand > 0.6666 : startXA = tmpObj.bucketXOffset;
            tobj = tmpObj.dumbbelsA[dumbbellIndex];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(startXA, tmpObj.defenseHeight * (tmpObj.dumbbellHeight / tmpObj.idealHumanHeadHeights ), tmpObj.backDistBucket);
            tobj.endPos.set(0, tmpObj.defenseHeight * (tmpObj.dumbbellHeight / tmpObj.idealHumanHeadHeights ), 0);
            if random.random() < 0.1 : 
                insideI = abs(startXA) < 0.1;
                startYA = tmpObj.defenseHeight - 0.16 - 0.25 * tmpObj.backDistBucket if insideI else tmpObj.defenseHeight - 0.16 + 0.25 * tmpObj.bucketHypotenuse;
                tobj.strtPos.y = startYA;
            tobj.strtTime = strtTimeA;
            tobj.endTime = tobj.strtTime + tmpObj.flightTimeDumbbell;
            self.postAdjustEndpos(tmpObj, tobj.endPos);
            self.enableStart(tmpObj, tobj);

    # initIntervalDisruptiveDumbbell




    # Generates a disruptive dumbbell in sequence at the start time.
    def initSequenceDisruptiveDumbbell(self, tmpObj : SceneGenerator.SceneGenerator , strtTimeI : float , dumbbellIndex : int ) :

        strtTimeA = strtTimeI;
        rand = random.random();
        startXA = 0;
        if rand < 0.3333 : startXA = -tmpObj.bucketXOffset;
        if rand > 0.6666 : startXA = tmpObj.bucketXOffset;
        tobj = tmpObj.dumbbelsA[dumbbellIndex];
        tobj.strtPos = Vec3.Vec3();
        tobj.endPos = Vec3.Vec3();
        tobj.strtPos.set(startXA, tmpObj.defenseHeight * (tmpObj.dumbbellHeight / tmpObj.idealHumanHeadHeights ), tmpObj.backDistBucket);
        tobj.endPos.set(0, tmpObj.defenseHeight * (tmpObj.dumbbellHeight / tmpObj.idealHumanHeadHeights ), 0);
        if random.random() < 0.1 :
            insideI = abs(startXA) < 0.1;
            startYA = tmpObj.defenseHeight - 0.16 - 0.25 * tmpObj.backDistBucket if insideI else tmpObj.defenseHeight - 0.16 + 0.25 * tmpObj.bucketHypotenuse;
            tobj.strtPos.y = startYA;
        tobj.strtTime = strtTimeA;
        tobj.endTime = tobj.strtTime + tmpObj.flightTimeDumbbell;
        self.postAdjustEndpos(tmpObj, tobj.endPos);
        self.enableStart(tmpObj, tobj);

    # initSequenceDisruptiveDumbbell
 
 
