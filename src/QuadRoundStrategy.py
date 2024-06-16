


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

from ContainerStrategy import ContainerStrategy


# Strategy with four rounds of an offensive strategy followed by a defensive strategy.
class QuadRoundStrategy(Strategy.Strategy):
    
    # Initializes an instance of the strategy.
    def init(self, tmpObj : SceneGenerator.SceneGenerator , strtTimeI : float ) :

        strategies = [];

        INCHES_TO_CENTIMETERS = 2.54;
        CENTIMETERS_TO_METERS = 0.01;
        FEET_TO_INCHES = 12;

        if (tmpObj.offenseHeight - tmpObj.defenseHeight) > (2 * INCHES_TO_CENTIMETERS * CENTIMETERS_TO_METERS) : 
            
            strategies = [ None ] * 12
            
            strategies[0] = tmpObj.rightUppercutStrategy;

            strategies[1] = tmpObj.leftUppercutStrategy;

            strategies[2] = tmpObj.rightFrontKickAbdomenStrategy;

            strategies[3] = tmpObj.leftFrontKickAbdomenStrategy;

            strategies[4] = tmpObj.rightRoundhouseKickStrategy;

            strategies[5] = tmpObj.leftRoundhouseKickStrategy;

            strategies[6] = tmpObj.rightUppercutJumpStrategy;

            strategies[7] = tmpObj.leftUppercutJumpStrategy;

            strategies[8] = tmpObj.rightSideBladeKickAbdomenStrategy;

            strategies[9] = tmpObj.leftSideBladeKickAbdomenStrategy;

            strategies[10] = tmpObj.rightSideBladeKickTrainAbdomenStrategy;

            strategies[11] = tmpObj.leftSideBladeKickTrainAbdomenStrategy;
            
        else : 
            
            strategies = [ None ] * 16
            
            strategies[0] = tmpObj.rightHookHeadStrategy;

            strategies[1] = tmpObj.leftHookHeadStrategy;

            strategies[2] = tmpObj.rightUppercutStrategy;

            strategies[3] = tmpObj.leftUppercutStrategy;

            strategies[4] = tmpObj.rightFrontKickAbdomenStrategy;

            strategies[5] = tmpObj.leftFrontKickAbdomenStrategy;

            strategies[6] = tmpObj.rightRoundhouseKickStrategy;

            strategies[7] = tmpObj.leftRoundhouseKickStrategy;

            strategies[8] = tmpObj.rightUppercutJumpStrategy;

            strategies[9] = tmpObj.leftUppercutJumpStrategy;

            strategies[10] = tmpObj.leftHammerStrikeStrategy;

            strategies[11] = tmpObj.rightHammerStrikeStrategy;

            strategies[12] = tmpObj.rightSideBladeKickAbdomenStrategy;

            strategies[13] = tmpObj.leftSideBladeKickAbdomenStrategy;

            strategies[14] = tmpObj.rightSideBladeKickTrainAbdomenStrategy;

            strategies[15] = tmpObj.leftSideBladeKickTrainAbdomenStrategy;
        # if


        strategiesD = [ None ] * 2;

        strategiesD[0] = tmpObj.dumbbellStrategy;

        strategiesD[1] = tmpObj.jumpHurdleStrategy;




        str9 = ContainerStrategy();
        randn = random.randrange( len( strategies ) )
        str9.immediateSequence = strategies[randn];
        str9.nextSequence = None;


        str8 = ContainerStrategy();
        randn = random.randrange( len( strategiesD ) )
        str8.immediateSequence = strategiesD[randn];
        str8.nextSequence = str9;


        str7 = ContainerStrategy();
        randn = random.randrange( len( strategies ) )
        str7.immediateSequence = strategies[randn];
        str7.nextSequence = str8;


        str6 = ContainerStrategy();
        randn = random.randrange( len( strategiesD ) )
        str6.immediateSequence = strategiesD[randn];
        str6.nextSequence = str7;


        str5 = ContainerStrategy();
        randn = random.randrange( len( strategies ) )
        str5.immediateSequence = strategies[randn];
        str5.nextSequence = str6;


        str4 = ContainerStrategy();
        randn = random.randrange( len( strategiesD ) )
        str4.immediateSequence = strategiesD[randn];
        str4.nextSequence = str5;


        str3 = ContainerStrategy();
        randn = random.randrange( len( strategies ) )
        str3.immediateSequence = strategies[randn];
        str3.nextSequence = str4;


        str2 = ContainerStrategy();
        randn = random.randrange( len( strategiesD ) )
        str2.immediateSequence = strategiesD[randn];
        str2.nextSequence = str3;


        randn = random.randrange( len( strategies ) )
        strategies[randn].init(tmpObj, strtTimeI);
        tmpObj.nextSequence = str2;

    # init
    

 
 
