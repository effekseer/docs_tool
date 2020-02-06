=====================
Reference(Material)
=====================

Overview
========================

Effekseer allows you to create materials for use with the Material Editor.
You can use materials to specify how particles are drawn.

The Material Editor starts from Material in the Effekseer Basic Render Settings Panel.

In the Material Editor, you can use nodes to write calculations.
The result of the calculation is drawn as particles.



.. image:: ../../img/Reference/Material/example_material_effect.png
   :scale: 80%
   :align: center

.. image:: ../../img/Reference/Material/example_material_node.png
   :scale: 80%
   :align: center


You can connect the input and output of the node with the left mouse drag.

You can create a new node from the right-click menu.

.. image:: ../../img/Reference/Material/node_menu_ja.png
   :scale: 80%
   :align: center

The simplest design has two nodes: Constant3 and Output.

For Constant3, you can specify three values.
On Output, you receive the final output value.

You connect the output Emissive input pin and the Constant3 output pin.

Then, the value of Constant3 is displayed on the particle.

.. image:: ../../img/Reference/Material/basic_ja.png
   :scale: 80%
   :align: center

Detailed operation method
========================

Move node
------------------------

After selecting with left click, you can move with left drag.

Search node
------------------------

If you enter a keyword in the menu with right-click, only the nodes that contain that keyword are displayed.
Keyword is shown by mouse over.

TODO : 図

Delete line or node
------------------------

Left-click to select and right-click to display Delete in the menu.
Select Delete to delete nodes and lines.

TODO : 図

Description of parameters
------------------------

A summary and description can be written in the parameter node.
This summary and description are displayed in Effekseer.
I recommend that you write a clear description.

Shortcut
------------------------

Ctrl + Z - Undo
Ctrl + Y - Redo
Ctrl + C - Copy
Ctrl + V - Paste
Ctrl + S - Save

About lighting
========================

You can select whether are particles lighttten with Outout node in a material.

TODO : 図

Value types of input and output
========================

There are two value types: Number and Image.
Number in the material consists of 1 to 4 numerical values.
In many cases, Number can be connected with different number of elements.
Image can only be connected to image.

In this document, I call Number 1 to Number 4 depending on the number of elements.


Node
========================

There are various nodes in the material editor.

Output
------------------------

You can specify the final output value.

In the output, you can set the type of lighting.

Currently, there are Lit and Unlit lighting.
If you specify Lit, it will be affected by the light source.
If you specify Unlit, the entered value is displayed.

TODO : 画像

BaseColor (Number3)
^^^^^^^^^^^^^^^^^^^^^^^^

Valid only for Lit. Enter the color of the material.

Emissive (Number3)
^^^^^^^^^^^^^^^^^^^^^^^^

Enter the emission color of the material.
For Unlit, enter the color to display.

Opacity (Number1)
^^^^^^^^^^^^^^^^^^^^^^^^

Enter the transparency.

OpacityMask (Number1)
^^^^^^^^^^^^^^^^^^^^^^^^

Enter the mask. If it is less than 0, it will not be displayed at all.

Roughness (Number1)
^^^^^^^^^^^^^^^^^^^^^^^^

Valid only for Lit. Enter the surface roughness.

Normal (Number3)
^^^^^^^^^^^^^^^^^^^^^^^^

Valid only for Lit. Enter the direction of the normal.

AmbientOcclusion
^^^^^^^^^^^^^^^^^^^^^^^^

Valid only for Lit. Enter a value to darken the lighting.
Set to 0 to make it black.

WorldPositionOffset (Number3)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Enter the moving distance of the vertex.
The vertex position moves by the entered value.

Refraction (Number1)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Enter the refractive index. If the refractive index is 1, it will not be refracted.
If the refractive index does not appear, enter the background by refracting it.
Enter a value of 1 or more.

Comment (Comment)
------------------------

Comments for clarity. Does not affect operation.

.. toctree::
    :maxdepth: 1

    material_NodeMath
    material_NodeImage
    material_NodeModel
    material_NodeConstant

Details of calculation behavior
========================

If V1 and V2 have inputs, you can enter the same type of value or the number 1 for V2.
If V1 and V2 are of the same type, the result calculated for each element is output.

If V1 is the numerical value 1, it outputs each element of V2 and the result of calculating V1.
If V2 is the number 1, the result of calculating each element of V1 and V2 is output.