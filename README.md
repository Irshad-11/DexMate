<div align="center">

  <!-- Banner: replace the src with your image URL -->
  <img src="https://github.com/Irshad-11/Documents/blob/c6bec49896545484cc047b6d94586e7d1851a577/Gemini_Generated_Image_2gcxlg2gcxlg2gcx.png" alt="Project Banner" width="100%" />

  <h1>DexMate</h1>
  <p>Lightweight Pokémon database that uses PokeAPI to fetch data in real time and show results based on user input.</p>

  <!-- Optional badges (replace or remove as needed) -->
  <p>
    <img alt="CI Status" src="https://img.shields.io/badge/CI-GitHub%20Actions-blue" />
    <img alt="Python" src="https://img.shields.io/badge/Python-3.x-yellow" />
  </p>
</div>

<hr />

<h2>Overview</h2>
<p>
  This repository is part of academic coursework and serves as a trial project for learning and practice.
  DexMate fetches Pokémon data from <a href="https://pokeapi.co">PokeAPI</a> and displays it based on user queries.
</p>

<h2>Features</h2>
<ul>
  <li><strong>Real-time data:</strong> Fetch Pokémon details from PokeAPI.</li>
  <li><strong>Simple queries:</strong> Search by name with clean outputs.</li>
  <li><strong>Lightweight design:</strong> Minimal dependencies and fast responses.</li>
  <li><strong>Automated CI:</strong> Build and test via GitHub Actions.</li>
</ul>



<h2>API</h2>
<ul>
  <li><strong>Base:</strong> <code>https://pokeapi.co/api/v2/</code></li>
  <li><strong>Pokémon endpoint:</strong> <code>/pokemon/{name_or_id}</code></li>
</ul>

<h2>CI/CD</h2>
<ul>
  <li><strong>CI workflow file:</strong> <code>ci.yml</code> — automates build and test on push/PR.</li>
  <li><strong>Build step:</strong> Install dependencies and create a clean artifact (<code>build.zip</code>).</li>
  <li><strong>Test step:</strong> Run Pytest for API and core logic.</li>
</ul>

<h2>Testing</h2>
<ul>
  <li><strong>Framework:</strong> Pytest</li>
  <li><strong>Run tests:</strong> <code>pytest -q</code></li>
  <li><strong>Goal:</strong> Validate endpoints and responses, check status codes and data fields.</li>
</ul>


<h2>Credits</h2>
<ul>
  <li><strong>PokeAPI:</strong> <a href="https://pokeapi.co/">pokeapi.co</a></li>
  <li><strong>Author:</strong> Irshad Hossain</li>
</ul>
