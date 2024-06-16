


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


# Strategy for a train of punches to the abdomen starting from the left potentially followed by another higher strike.
class LeftStraightBodyTrainStrategy(Strategy.Strategy):
    
    
    # Initializes an instance of a segment of the strategy.
    def initSegment(self, tmpObj : SceneGenerator.SceneGenerator, strtTimeI : float, randx : float , punchIndex : int ) :

        

        split2 = tmpObj.referenceTimeSplit;
        split3 = 0.75 * split2;

        strtTimeA = strtTimeI;





        tmpObj.leftStraightAbdomenStrategy.initSegment(tmpObj, strtTimeA, randx, punchIndex);




        strtTimeA = strtTimeI + 2 * split3 + 2 * split2;





        tmpObj.rightStraightAbdomenStrategy.initSegment(tmpObj, strtTimeA, randx, punchIndex);









    
    
    # Initializes an instance of the strategy.
    def init(self, tmpObj : SceneGenerator.SceneGenerator , strtTimeI : float ) :

        split2 = tmpObj.referenceTimeSplit;
        randx = random.random();
        split3 = 0.75 * split2;

        strtTimeA = strtTimeI;


        self.initSegment(tmpObj, strtTimeA, randx, 0);


        self.initSegment(tmpObj, strtTimeA + 4 * split2 + 4 * split3, randx, 3);

        endIndex = 6;
        endSplit2 = 8;
        endSplit3 = 8;
        fEnd = tmpObj.flightTimeStraightPunch;


        if random.random() > 0.5 : 
            # Nothing
            xx = 1
        else :
            self.initSegment(tmpObj, strtTimeA + endSplit2 * split2 + endSplit3 * split3, randx, 6);

            endSplit2 = endSplit2 + 4;
            endSplit3 = endSplit3 + 4;
            endIndex = 9;
        # else
        tmpObj.dumbbellStrategy.initPotentialDisruptiveDumbbell(tmpObj, strtTimeI, tmpObj.endTime);


        if random.random() < 0.5 : 
            if random.random() > 0.25 :
                tmpObj.leftUppercutStrategy.initSegment(tmpObj, strtTimeA + endSplit2 * split2 + endSplit3 * split3, randx, endIndex);
                fEnd = tmpObj.flightTime;
                endSplit2 = endSplit2 + 4;
            else :
                tmpObj.dumbbellStrategy.initSequenceDisruptiveDumbbell(tmpObj, strtTimeA + endSplit2 * split2 + endSplit3 * split3, 0);
                fEnd = tmpObj.flightTimeStraightPunch;
                endSplit2 = endSplit2 + 2;
            # else
        # if


        tmpObj.endTime = strtTimeA + (endSplit2 - 2) * split2 + endSplit3 * split3 + fEnd;


    # init
    

 
 
