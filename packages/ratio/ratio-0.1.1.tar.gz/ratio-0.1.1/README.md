<h1 align="center">Ratio</h1>
<p align="center">
  The Python web framework for developers who want to get shit done.
</p>
<hr />
<strong>Ratio is currently being developed and all releases in this phase may introduce breaking changes until further notice.
Please do not use Ratio in production without carefully considering the consequences.</strong>
<hr />
<h2>What is Ratio?</h2>
<p>
  Ratio is an asynchronous Python web framework that was built with developer experience in mind. Quick to learn for those
  who just start out with programming and powerful so that senior developers can build high performance web applications 
  with it. The framework is designed with the Goldilocks principle in mind: just enough. Enough power to run high performance
  web applications, enough intuitive design, so that developers can easily pick up on the principles.
</p>
<p>
  Ratio borrows ideas from great frameworks, like <a href="https://github.com/django/django" target="_blank">Django</a>, 
  <a href="https://github.com/tiangolo/fastapi" target="_blank">FastAPI</a> and <a href="https://github.com/vercel/next.js" target="_blank">Next.js</a>, 
  and combines them with original concepts to improve the life of a developer when creating web applications for any
  purpose.
</p>
<h2>Ready out of the box</h2>
<p>
  Ratio will be shipped with a custom and extensible command line interface, which can be used to perform actions within a
  project.
</p>
<p>
  This is what we aim Ratio to do:<br>
  <small>This list is not complete and will be extended after certain releases in the pre-release phase.</small>
</p>

<ul>
  <li><strong>File based routing:</strong> Intuitive routing for each incoming request, based on file system.</li>
  <li><strong>Integrates with databases:</strong> Connect to SQL or SQLite databases from within the application controllers.</li>
  <li><strong>Write once, use everywhere:</strong> Do not repeat yourself, by defining models, routes and actions you can use them throughout the application.</li>
  <li><strong>Adheres to standards:</strong> API views are based on <a href="">OpenAPI</a> and the JSON schema standard.</li>
</ul>


<h2>Minimal external dependencies</h2>
<p>
  Currently, Ratio only requires the <code>rich</code> package from outside the Python standard library, which is used 
  for rendering beautiful output to the command line. In a future version of Ratio, we might want to remove this direct
  dependency for users who really want to have no external dependencies.
</p>