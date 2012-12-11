IE-Bullet-Fix
=============

Version: 1.0
Author: [Jordan Mack](http://jmack.parhelic.com)

A simple CSS workaround to the IE bug that causes bulleted lists to display incorrectly, or with tiny bullets that cannot be resized properly. This fix corrects the bullets by replacing them with static images. The images are inlined in the CSS for convinience.

The source image files, and a Python script to generate the base64 strings, are included in the bundle.

##Installation

Copy the file **iebulletfix.css** into your website's CSS folder, and include the following conditional comment in your website's **&lt;head&gt;** section:

    <!--[if IE]>
    <link rel="stylesheet" type="text/css" href="/path/to/css/iebulletfix.css" />
    <![endif]-->

Next add the class **iebulletfix** to the **UL** tag of the list in question:

    <ul class="iebulletfix">

You may need to tweak the padding within **iebullettfix.css** to match your page.

Please use **iebulletfix.html** as an example for common usage.

##Notes
This fix uses static images, which will not scale according to the font sizes on your page. This fix should only be used as a last resort when the IE bug is present, and no other CSS workaround can be found.

