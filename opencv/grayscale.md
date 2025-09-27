<h1>Theory related to Grayscale images and how they are formed?</h1>

<p> Grayscale conversion is the conversion of 2 different channels RGB in the same order into a single-channel image where <br> each pixel represents channel luminosity or intensity. <br>

<h2>Common Grayscale Conversion Images : </h2><br>
<h3>1. Luminosity Method : Weighted Average of the 3 channels </h3> 
<p> This is the most accurate as this is based on how colors are percieved by the human eye. Green is the most sensitive to the human eye, followed by red and then blue. </p>
<b><i> Gray = 0.299R + 0.587G + 0.114B</i></b>

<h3>2. Average Method </h3> 
<p> This is the simplest method for the conversion but least accurate </p>
<b><i> Gray = (R+G+B)/3 </i></b>

<h3>3. Lightness Method </h3> 
<p> While this method is straightforward, it can reduce the overall intensity of the image. </p>
<b><i> Gray = max(R,G,B) + min(R,G,B) </i></b>



