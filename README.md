# INI file parser

<h2>This program helps you to parse ini files.</h2>

<p>It has couple parametrs, such as: <br>
"-p" –– absolute path to the ini file,<br>
"-s" –– section, you want to get info from,<br>
"-o" –– option in the section and <br>
"-t" –– type of value you are expecting to get.</p>

<h3>Rules of parsing:</h3>
<ul>
    <li>All that goes after ';' is considered a comment and ignored.</li>
    <li>Signs that are allowed in section and option names are signs of Latin alphabet, numbers, and underscores. </li>
</ul>

<h3>Example of the input:</h3>
<code>python INI_pars.py -p 'exp.ini' -s 'DEFAULT' -o 'ServerAliveInterval' -t 'int'</code>
<h3>Expecting output</h3>
<strong>45</strong>
