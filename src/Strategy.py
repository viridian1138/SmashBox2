


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



from abc import ABCMeta, abstractmethod

import random

import SceneGenerator
import Target
import Vec3


class Strategy(object):
    __metaclass__ = ABCMeta
    
    """
    # Abstract method that initializes the strategy into the SceneGenerator
    #
    """
    @abstractmethod
    def init(self, tmpObj : SceneGenerator.SceneGenerator , strtTime : float ):
        raise NotImplementedError


    # Rotates a position near the player camera based on the input rand value.
    def randRotateClose( self , tmpObj : SceneGenerator.SceneGenerator , rand : float , locn : Vec3.Vec3 ) :
        if rand > 0.6666 :
            return;

        bucketCosine = tmpObj.bucketCosine;

        bucketSine = tmpObj.bucketSine;

        if rand < 0.33333 : 
            bucketSine = - bucketSine;

        xx = locn.x;

        yy = locn.z;

        xx2 = xx * bucketCosine - yy * bucketSine;

        yy2 = xx * bucketSine + yy * bucketCosine;

        locn.x = xx2;

        locn.z = yy2;

    # randRotateClose




    # Rotates a far position near the buckets based on the input rand value.
    def randRotateFar( self, tmpObj : SceneGenerator.SceneGenerator, rand : float , locn : Vec3.Vec3 ) : 
        if rand > 0.6666 : 
            return;


        self.randRotateClose(tmpObj, rand, locn);

        locn.x = locn.x * tmpObj.bucketDistRatio;

        locn.z = locn.z * tmpObj.bucketDistRatio;


    # randRotateFar




    # Enables the starting of a target.
    def enableStart( self, tmpObj : SceneGenerator.SceneGenerator, tobj : Target.Target ) :
        tobj.timeEnabled = True;
        tobj.mesh.dynamicSetPosn(0, 0, tmpObj.targetFarDist, tmpObj.dynamicPosnList);
        tobj.collided = False;
        tobj.collisionEnable = True
        tobj.initialStart = True;
    # enableStart





    # Adjusts the end position using the current position of the player camera.
    def postAdjustEndpos( self, tmpObj : SceneGenerator.SceneGenerator , endPos : Vec3.Vec3 ) :
        cameraPos = tmpObj.hmdLocn
        endPos.x = endPos.x + cameraPos.x;
        endPos.z = endPos.z + cameraPos.z;
    # postAdjustEndpos
    
    
    
    
    # Returns a random-generated delay time to vary the periods between strategies and/or the periods between parts of strategies.
    def xDeltaTime( self , flightTime : float ) : 
        if random.random() < 0.3333333 :
            at0 = 0.8 * flightTime;
            at1 = 0.9 * flightTime;
            at2 = 1.0 * flightTime;
            rndd = random.random();
            if rndd < 0.333333 :
                return( at0 * random.random() );
            elif rndd < 0.66666 :
                u = random.random();
                return( (1-u) * at0 + u * at1 );
            else : 
                u = random.random();
                return( (1-u) * at1 + u * at2 );
        else :
            return( 0 );
    # xDeltaTime
 
 
