# Kill Rules

## Overview

Kill Rules allows to specify area in which particles should be destroyed. 
If particle has configured fade out it will be applied before removal.

While in Editor you can select a node in node tree to preview it's 
configured kill rule shape. 

## Box

Box used to kill particles when they're either inside or outside the defined box.


```eval_rst
.. image:: ../../img/Reference/killRules_Box.png
   :align: center
```


#### Center

Position of the center of the box in effect space.

#### Size

Extents of the box around it's center. 
For example, if size is set to (0.5, 0.5, 0.5) box will have width, height and depth of 1.

#### Kill Inside

If enabled, particles will be killed when they fall INSIDE the box.
If disabled (the default), they will be killed when they fall OUTSIDE the box.

#### Scale And Position Applied

If enabled (the default) box will be rotated and scaled with effect.
If disabled the box will be axis aligned and with fixed size.

## Plane

Plane used to kill particle when it moves beyond certain position along specified axis.


```eval_rst
.. image:: ../../img/Reference/killRules_Plane.png
   :align: center
```

#### Plane Axis

Defines axis with which plane's normal will be aligned. 
Inverting the axis allows to change to the side on which particles will be killed.

For example, if axis is set +Y particles will be killed when they are above the plane, 
but if you set axis to -Y particles will be killed when they are below the plane. 

#### Plane Offset Along Axis

Defines how far plane will be moved along it's axis. 
For example, if axis is set to +Y and plane offset is 1.0, then particles will be killed when they Y position is greater than 1.0,
but if axis is set to -Y and plane offset is 1.0, then particles will be killed when they Y position is less than -1.0.

#### Scale And Position Applied

If enabled (the default) plane orientation will be rotated when effect orientation changes 
and plane's offset will be scaled with effect's scale.
If disabled the plane orientation will remain fixed and it's offset wont change with effect scale.

## Sphere

Sphere used to kill particle when it moves inside or outside of the specified sphere.


```eval_rst
.. image:: ../../img/Reference/killRules_Sphere.png
   :align: center
```

#### Center

Position of the center of the sphere in effect space.

#### Radius

Radius of the sphere.

#### Kill Inside

If enabled, particles will be killed when they fall INSIDE the sphere.
If disabled (the default), they will be killed when they fall OUTSIDE the sphere.

#### Scale And Position Applied

If enabled (the default) sphere position will be rotated relative to effect's space origin and sphere's 
radius will be scaled with effect's scale.
If disabled the sphere position will remain at the constant position relative to effect's space origin and radius will be fixed.