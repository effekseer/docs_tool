# Procedural Model

## Overview

This function allows you to create a 3D model by simply adjusting the parameters.
Normally, you would need to use other software to create a 3D model, but you can create a simple 3D model within Effekseer.

## Parameters

### Type

Specifies the type of mesh to be generated.

#### mesh

Generates the outer mesh of a sphere or cylinder, depending on the specified parameters.
Basically, it generates a rotating object about an axis.

##### Range (angle)

Specifies the range of rotators to be generated.
Normally, it is a circle, but it can be made into a cut out part of it.

````eval_rst
... image:: .../.../img/Reference/ProceduralModel/Angle.png
   :align: center
````

##### Number of splits

The number of divisions of the mesh.The larger this value is, the smoother it becomes.

````eval_rst
... image:: .../.../img/Reference/ProceduralModel/Division.png
   :align: center
````

#### ribbon

Generates a shape that looks like it wraps around the mesh.

##### cross-section

Specify the shape of the ribbon section.

- plane

````eval_rst
... image:: .../.../img/Reference/ProceduralModel/Ribbon.png
   :align: center
````

- cross

````eval_rst
... image:: .../.../img/Reference/ProceduralModel/Ribbon_Cross.png
   :align: center
````

- point

It is not displayed as a mesh, but can be used as a parameter for the generation position.

````eval_rst
... image:: .../.../img/Reference/ProceduralModel/Ribbon_Point.png
   :align: center
````

##### Rotation angle

Specifies the amount of angle at which the ribbon rotates about its axis.

````eval_rst
... image:: .../.../img/Reference/ProceduralModel/Ribbon_Rotation.png
   :align: center
````

##### Thickness

Specifies the thickness of the ribbon at the start and end points.

````eval_rst
... image:: .../.../img/Reference/ProceduralModel/Ribbon_Thickness.png
   :align: center
````

##### angle

Specifies the amount of rotation from the viewpoint to the end point per ribbon.

````eval_rst
... image:: .../.../img/Reference/ProceduralModel/Ribbon_Angle.png
   :align: center
````

##### Noise (length)

Move the ribbon and the start and end points randomly.

````eval_rst
... image:: .../.../img/Reference/ProceduralModel/Length_Noise.png
   :align: center
````

##### Number of bottles

Specifies the number of ribbons.

````eval_rst
... image:: .../.../img/Reference/ProceduralModel/Ribbon_Count.png
   :align: center
````

### Type of shape

Specify the mesh shape of the actual model to be generated.

#### ball

Sphere.
You can specify which region of the sphere is to be specified.

````eval_rst
... image:: .../.../img/Reference/ProceduralModel/Sphere.png
   :align: center
````

#### cone

Corn.
Radius and depth can be specified.

````eval_rst
... image:: .../.../img/Reference/ProceduralModel/Cone.png
   :align: center
````

#### cylinder

Cylinders.
You can specify different values for the top and bottom radii of the cylinder.
It can also be made into a disk by setting the depth to 0.

````eval_rst
... image:: .../.../img/Reference/ProceduralModel/Cylinder.png
   :align: center
````

#### spline

This is a rotator with four points specifying the sides.
This is useful for expressing tornadoes, auras, etc.

````eval_rst
... image:: .../.../img/Reference/ProceduralModel/Spline.png
   :align: center
````

### Axis

Specifies in which direction the mesh will be generated.

````eval_rst
... image:: .../.../img/Reference/ProceduralModel/Axis.png
   :align: center
````

### Noise

It distorts the generated shape.

#### tilt-noise

Causes the mesh to tilt at each axial position.
It is suitable for creating meshes that are diagonal in each part, such as tornadoes.

````eval_rst
... image:: .../.../img/Reference/ProceduralModel/Tilt.png
   :align: center
````

#### wave noise

Shake each position of the model with a wave.
It is good for generating meshes that look like they are shaken by waves at regular intervals.

````eval_rst
... image:: .../.../img/Reference/ProceduralModel/Wave.png
   :align: center
````

#### curl-noise

For each position of the model, distort it in a random direction.

````eval_rst
... image:: .../.../img/Reference/ProceduralModel/Curl.png
   :align: center
````

### Vertex color

Specify a color for each position and interpolate the colors between them.

````eval_rst
... image:: .../.../img/Reference/ProceduralModel/VertexColors.png
   :align: center
````

#### Central Region Percentage

Specifies how much the center color specified by the vertex color will occupy the center area.
The larger this value is, the more area the central vertex color occupies.

````eval_rst
... image:: .../.../img/Reference/ProceduralModel/VertexColors_CenterArea.png
   :align: center
````