﻿# 概要

## 操作环境和所需的运行时

### 编辑工具（Windows）

Windows7 SP1或之后的版本

DirectX 11（ShaderModel 4.0或之后的版本）

如果程序不能运行，请通过以下链接安装D3DCompiler_47.dll。

[D3DCompiler_47.dll](https://support.microsoft.com/en-us/help/4020302/the-net-framework-4-7-installation-is-blocked-on-windows-7-windows-ser)

### 编辑工具（macOS）

macOS Sierra或之后的版本

如果程序不能运行，请通过以下链接安装mono。

[mono](https://www.mono-project.com/)

### 运行时

*   DirectX 9（ShaderModel 3.0或之后的版本）
*   DirectX 11（ShaderModel 3.0或之后的版本）
*   OpenGL 4.1或之后的版本
*   OpenGL ES 2.0或之后的版本

## 安装/卸载

### Windows

编辑器整个位于“Tool/”文件夹下。我们未对注册表和其他东西做任何修改。你可以直接启动程序，或将其复制到任何文件夹。
卸载的方式就是删除文件夹。

### macOS

打开Effekseer.dmg并将Effekseer.app复制到Applications或Home文件夹。
卸载Effekseer的方式是删除Effekseer.app。

### 其他

要在游戏中播放特效，必须下载单独的包，例如运行时、Unity或者DX库。

此外，如果只想将特效导出为图片、精灵表单（Sprite Sheet）或视频，参考[录像](ToolReference/record)。

## 许可证

运行时以MIT许可证发布。

使用DirectX时，依赖[DirectX Tool Kit](https://directxtk.codeplex.com/)。

使用Vulkan时，依赖[glslang](https://github.com/KhronosGroup/glslang)。

具体请参考下面的许可证。

纹理和特效数据以CC-0协议发布。你可以任意使用。

## 免责声明

对于使用本软件和运行时可能出现的任何问题，我们不承担任何责任。

## 联系方式

effekseer(at)gmail.com

## 版权声明

### 许可证（运行时）

<pre>
The MIT License (MIT)

Copyright (c) 2011 Effekseer Project

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

</pre>

### 许可证（编辑器）

<pre>
The MIT License (MIT)

Copyright (c) 2011 Effekseer Project

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

DirectX Tool Kit
https://directxtk.codeplex.com/
Microsoft Public License (Ms-PL)

Lumix Engine is licensed under the MIT License
Copyright (c) 2013-2016 Mikulas Florek

imgui is licensed under the MIT License
Copyright (c) 2014-2018 Omar Cornut

Boxer is licensed under the MIT License
Copyright (c) 2014 Aaron Jacobs

GD Graphics Library

Credits and license terms:

In order to resolve any possible confusion regarding the authorship of
gd, the following copyright statement covers all of the authors who
have required such a statement. If you are aware of any oversights in
this copyright notice, please contact Pierre-A. Joye who will be
pleased to correct them.

   Portions copyright 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001,
   2002, 2003, 2004 by Cold Spring Harbor Laboratory. Funded under
   Grant P41-RR02188 by the National Institutes of Health.

   Portions copyright 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
   2004 by Boutell.Com, Inc.

   Portions relating to GD2 format copyright 1999, 2000, 2001, 2002,
   2003, 2004 Philip Warner.

   Portions relating to PNG copyright 1999, 2000, 2001, 2002, 2003,
   2004 Greg Roelofs.

   Portions relating to gdttf.c copyright 1999, 2000, 2001, 2002,
   2003, 2004 John Ellson (ellson@graphviz.org).

   Portions relating to gdft.c copyright 2001, 2002, 2003, 2004 John
   Ellson (ellson@graphviz.org).

   Portions copyright 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007
   Pierre-Alain Joye (pierre@libgd.org).

   Portions relating to JPEG and to color quantization copyright
   2000, 2001, 2002, 2003, 2004, Doug Becker and copyright (C) 1994,
   1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004 Thomas
   G. Lane. This software is based in part on the work of the
   Independent JPEG Group. See the file README-JPEG.TXT for more
   information.

   Portions relating to GIF compression copyright 1989 by Jef
   Poskanzer and David Rowley, with modifications for thread safety
   by Thomas Boutell.

   Portions relating to GIF decompression copyright 1990, 1991, 1993
   by David Koblas, with modifications for thread safety by Thomas
   Boutell.

   Portions relating to WBMP copyright 2000, 2001, 2002, 2003, 2004
   Maurice Szmurlo and Johan Van den Brande.

   Portions relating to GIF animations copyright 2004 Jaakko Hyvätti
   (jaakko.hyvatti@iki.fi)

Permission has been granted to copy, distribute and modify gd in
any context without fee, including a commercial application,
provided that this notice is present in user-accessible supporting
documentation.

This does not affect your ownership of the derived work itself,
and the intent is to assure proper credit for the authors of gd,
not to interfere with your productive use of gd. If you have
questions, ask. "Derived works" includes all programs that utilize
the library. Credit must be given in user-accessible
documentation.

This software is provided "AS IS." The copyright holders disclaim
all warranties, either express or implied, including but not
limited to implied warranties of merchantability and fitness for a
particular purpose, with respect to this code and accompanying
documentation.

Although their code does not appear in the current release, the
authors also wish to thank Hutchison Avenue Software Corporation
for their prior contributions.

Native File Dialog

This software is provided 'as-is', without any express or implied
warranty.  In no event will the authors be held liable for any damages
arising from the use of this software.

Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it
freely, subject to the following restrictions:

1\. The origin of this software must not be misrepresented; you must not
   claim that you wrote the original software. If you use this software
   in a product, an acknowledgment in the product documentation would be
   appreciated but is not required.
2\. Altered source versions must be plainly marked as such, and must not be
   misrepresented as being the original software.
3\. This notice may not be removed or altered from any source distribution.

-- 源真ゴシック --

This Font Software is licensed under the SIL Open Font License, Version 1.1.
This license is copied below, and is also available with a FAQ at:
http://scripts.sil.org/OFL

-----------------------------------------------------------
SIL OPEN FONT LICENSE Version 1.1 - 26 February 2007
-----------------------------------------------------------

PREAMBLE
The goals of the Open Font License (OFL) are to stimulate worldwide
development of collaborative font projects, to support the font creation
efforts of academic and linguistic communities, and to provide a free and
open framework in which fonts may be shared and improved in partnership
with others.

The OFL allows the licensed fonts to be used, studied, modified and
redistributed freely as long as they are not sold by themselves. The
fonts, including any derivative works, can be bundled, embedded, 
redistributed and/or sold with any software provided that any reserved
names are not used by derivative works. The fonts and derivatives,
however, cannot be released under any other type of license. The
requirement for fonts to remain under this license does not apply
to any document created using the fonts or their derivatives.

DEFINITIONS
"Font Software" refers to the set of files released by the Copyright
Holder(s) under this license and clearly marked as such. This may
include source files, build scripts and documentation.

"Reserved Font Name" refers to any names specified as such after the
copyright statement(s).

"Original Version" refers to the collection of Font Software components as
distributed by the Copyright Holder(s).

"Modified Version" refers to any derivative made by adding to, deleting,
or substituting -- in part or in whole -- any of the components of the
Original Version, by changing formats or by porting the Font Software to a
new environment.

"Author" refers to any designer, engineer, programmer, technical
writer or other person who contributed to the Font Software.

PERMISSION & CONDITIONS
Permission is hereby granted, free of charge, to any person obtaining
a copy of the Font Software, to use, study, copy, merge, embed, modify,
redistribute, and sell modified and unmodified copies of the Font
Software, subject to the following conditions:

1) Neither the Font Software nor any of its individual components,
in Original or Modified Versions, may be sold by itself.

2) Original or Modified Versions of the Font Software may be bundled,
redistributed and/or sold with any software, provided that each copy
contains the above copyright notice and this license. These can be
included either as stand-alone text files, human-readable headers or
in the appropriate machine-readable metadata fields within text or
binary files as long as those fields can be easily viewed by the user.

3) No Modified Version of the Font Software may use the Reserved Font
Name(s) unless explicit written permission is granted by the corresponding
Copyright Holder. This restriction only applies to the primary font name as
presented to the users.

4) The name(s) of the Copyright Holder(s) or the Author(s) of the Font
Software shall not be used to promote, endorse or advertise any
Modified Version, except to acknowledge the contribution(s) of the
Copyright Holder(s) and the Author(s) or with their explicit written
permission.

5) The Font Software, modified or unmodified, in part or in whole,
must be distributed entirely under this license, and must not be
distributed under any other license. The requirement for fonts to
remain under this license does not apply to any document created
using the Font Software.

TERMINATION
This license becomes null and void if any of the above conditions are
not met.

DISCLAIMER
THE FONT SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT
OF COPYRIGHT, PATENT, TRADEMARK, OR OTHER RIGHT. IN NO EVENT SHALL THE
COPYRIGHT HOLDER BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
INCLUDING ANY GENERAL, SPECIAL, INDIRECT, INCIDENTAL, OR CONSEQUENTIAL
DAMAGES, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF THE USE OR INABILITY TO USE THE FONT SOFTWARE OR FROM
OTHER DEALINGS IN THE FONT SOFTWARE.

</pre>
