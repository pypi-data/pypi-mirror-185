<h1 align="center">Private Function in Python</h1>
<p align="center"><i>"A smarter way to create private functions in python"</i><p>
  
<h2 align="center">from <a href="https://faheem41.github.io" target="_blank" rel="noreferrer">FAHEEM41</br></a></h2>


<p>
  <ul>
    <li>version: <strong>1.5.23</strong></li>
    <li>first published in: <strong><a href="https://www.sololearn.com" target="_blank" rel="noreferrer">Sololearn</a></strong></li>
    <li>Github first publishing date: <strong>23rd July, 2022</strong></li>
    <li>Last Updated: <strong>11th January, 2023</strong></li>
  </ul>
</p>
</br>

<p>
<h2>Why use the code?</h2>
Let's start with the concept of private functions. Private functions are functions that are only accessible inside the declared module, no other function from any other module can access it.</br>
This project mainly focuses on the security issues of a code. This enables a way to restrict code from accessing other functions from other modules that were not meant to be accessed. And thus, it ensures that only non-private functions i.e. public functions can be accessed from anywhere outside the code.</br></br>
Here's an example, suppose a module has two functions: <i>add()</i> and <i>main()</i>. <i>main()</i> function is meant to run and can be called from other modules. On the other hand, the <i>add()</i> function is a function that is only called by the <i>main()</i> function, and we want to keep this function private, i.e. ensure that it cannot be accessed or called from any other module.
</p>
</br>

<p>
<h2>Understanding the code</h2>
Here we have implemented a very naive idea to get our work done. We have used a <i>decorator</i> which will check whether the function is a private or public function and thereby deny or grant access respectively. The <i>decorator</i> will run, as usual, with the function called, and before the function ran.</br>
For details understanding, have a look at the <a href="https://github.com/Faheem41/Private-Function-in-Python/blob/main/src/privatefunc.py" rel="noreferrer">privatefunc.py</a> file; the documentation of the code, along with how the code is working is given inside the source code.
</p>
</br>

<p>
<h2>How to use the code? (using pip)</h2>
In terminal type the command: <code>pip install privatefunc</code></br>
Add this lines in your module: </br><code>from privatefunc import PrivateFunc</code></br><code>private = PrivateFunc("nameOfThisModuleHere").private</code></br>
Now add <code>@private</code> before the function you want to make private</br></br>
For better understanding have a look at <a href="https://github.com/Faheem41/Private-Function-in-Python/blob/main/test/moduleWithPrivateFunc.py" rel="noreferrer">moduleWithPrivateFunc.py</a>
</p>
</br>

Everything put together:
```
# example.py
from privatefunc import PrivateFunc
private = PrivateFunc("example").private

@private
def hello():
    pass
```

<p>
<h2>Sample Code</h2>
Go through <a href="https://github.com/Faheem41/Private-Function-in-Python/tree/main/test" rel="noreferrer">the demo code</a> to completely understand the insights of the source.
</p>
</br>


<h6 align="center">© 2021-2023 Md. Faheem Hossain fmhossain2941@gmail.com</h6>
