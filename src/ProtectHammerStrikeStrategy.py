


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


# Strategy for an upper cross-block to protect from a hammer strike.


class ProtectHammerStrikeStrategy(Strategy.Strategy):
    
    # Initializes an instance of the strategy.
    def init(self, tmpObj : SceneGenerator.SceneGenerator , strtTimeI : float ) :

        split2 = tmpObj.referenceTimeSplit;

        strtTimeA = strtTimeI;
        strtTimeB = strtTimeI;

        if True :
            insideI = random.random() < 0.5;
            startXA = 0.08 if insideI else tmpObj.bucketXOffset;
            startYA = tmpObj.defenseHeight - 0.16 - 0.25 * tmpObj.backDistBucket if insideI else tmpObj.defenseHeight - 0.16 + 0.25 * tmpObj.bucketHypotenuse;
            tobj = tmpObj.targetsPunchB[0];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(startXA, startYA, tmpObj.backDistBucket);
            tobj.endPos.set(0.08, tmpObj.defenseHeight - 0.16, 0);
            tobj.strtTime = strtTimeA;
            tobj.endTime = tobj.strtTime + tmpObj.flightTime;
            self.postAdjustEndpos(tmpObj, tobj.endPos);
            self.enableStart(tmpObj, tobj);

            strtTimeA = tobj.endTime + self.xDeltaTime( tmpObj.flightTime );
        #if

        if True :
            insideI = random.random() < 0.5;
            startXB = -0.08 if insideI else -tmpObj.bucketXOffset;
            startYB = tmpObj.defenseHeight - 0.16 - 0.25 * tmpObj.backDistBucket if insideI else tmpObj.defenseHeight - 0.16 + 0.25 * tmpObj.bucketHypotenuse;
            tobj = tmpObj.targetsPunchA[0];
            tobj.strtPos = Vec3.Vec3();
            tobj.endPos = Vec3.Vec3();
            tobj.strtPos.set(startXB, startYB, tmpObj.backDistBucket);
            tobj.endPos.set(-0.08, tmpObj.defenseHeight - 0.16, 0);
            tobj.strtTime = strtTimeB;
            tobj.endTime = tobj.strtTime + tmpObj.flightTime;
            self.postAdjustEndpos(tmpObj, tobj.endPos);
            self.enableStart(tmpObj, tobj);

            strtTimeB = tobj.endTime;
        # if

        tmpObj.endTime = strtTimeA;
        if strtTimeB > strtTimeA :
            tmpObj.endTime = strtTimeB;
        #if 


    # init
    

 
 
