<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div>
<h3 align="center">Classroom Stats Visualizer</h3>

<p>
<h4 align="left">Problem Statement</h4>

K-12 educators need to be able to analyze a large set of data gathered from their 
classroom for determining the correct learning path for the class. Since the educators 
are currently looking at data from a table perspective, they are spending more time 
deciphering the data instead of planning the next learning activity. This is also a 
problem for the students, since educators are less focused on catering to their learning.

<h4 align="left">Solution Statement</h4>

The goal of Classroom Stats Visualizer is to analyze and determine a performance 
metric for each student given the student’s grades. This performance metric will 
allow for teachers to quickly determine which students are in need of assistance. 
Also, Classroom Stats Visualizer will provide teachers with the ability to dive 
deeper into each individual student. This deep dive will display the student’s 
performance metric along with generating visual aids based on student grades over 
the semester.
    </p>

</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## About The Project

### Built With

* [Django](https://www.djangoproject.com/)
* [Bootstrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)
* [Oracle Instant Client](https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->

## Getting Started

### Prerequisites

* Latest version of Python
<p align="right">(<a href="#top">back to top</a>)</p>

### Installation For Visual Studio Code (Windows)

1. Clone the repo
   ```sh
   git clone https://github.com/andrewkrawczyk/ClassroomStatsVisualizer
   ```
2. Generate Virtual Environment (~/ClassroomStatsVisualizer)
   ```sh
   py -3 -m venv .venv
   ```
3. Activate Environment
   ```sh
   .venv\scripts\activate
   ```
4. Move Directory
   ```sh
   cd .\DjangoWebProject 
   ```
5. Install Requirements
   ```sh
   pip3 install -r requirements.txt
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

### Installation For Instant Client (Windows)
1. Get a free Oracle wallet by emailing (blank)
2. Download the basic package (version 21.3) from the following link:
   https://www.oracle.com/database/technologies/instant-client/downloads.html
3. Unzip and place in the following directory
   ```sh
   C:\oracle\
   ```
4. Place the wallet into
   ```sh
   C:\oracle\instantclient_21_3\network\admin
   ```
   
### Running App For Visual Studio Code (Windows)
1. Unzip and place in the following directory
   ```sh
   python manage.py runserver
   ```
<p align="right">(<a href="#top">back to top</a>)</p>

### Installation For Visual Studio Code (macOS)

1. Clone the repo
   ```sh
   git clone https://github.com/andrewkrawczyk/ClassroomStatsVisualizer
   ```
2. Generate Virtual Environment (~/ClassroomStatsVisualizer)
   ```sh
   python3 -m venv .venv 
   ```
3. Activate Environment
   ```sh
   source .venv/bin/activate
   ```
4. Move Directory
   ```sh
   cd DjangoWebProject 
   ```
5. Install Requirements
   ```sh
   pip3 install -r requirements.txt
   ```
   
<p align="right">(<a href="#top">back to top</a>)</p>

### Installation For Instant Client (macOS)
1. Get a free Oracle wallet by emailing (blank)
2. Download the basic package (version 19.8) from the following link:
   https://www.oracle.com/database/technologies/instant-client/downloads.html
3. Unzip and place in the following directory
   ```sh
   ~/Downloads/instantclient_19_8
   ```
4. Place the wallet into
   ```sh
   ~/Downloads/instantclient_19_8/network/admin
   ```
<p align="right">(<a href="#top">back to top</a>)</p>

### Running App For Visual Studio Code (macOS)
1. Unzip and place in the following directory
   ```sh
   python3 manage.py runserver
   ```
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any
contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also
simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->

## Contact

CEN 3031: Group 6 - placeholder@comcast.net

Project Link: [https://github.com/andrewkrawczyk/ClassroomStatsVisualizer](https://github.com/github_username/repo_name)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge

[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge

[forks-url]: https://github.com/github_username/repo_name/network/members

[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge

[stars-url]: https://github.com/github_username/repo_name/stargazers

[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge

[issues-url]: https://github.com/github_username/repo_name/issues

[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge

[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]: https://linkedin.com/in/linkedin_username

[product-screenshot]: images/screenshot.png
