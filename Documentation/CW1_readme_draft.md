# Coursework 1

## Technical Information

### Repository URL

The following URL is a link to the repository for COMP0034 coursework 1 for group number 7:
[Repository Coursework 1 - Group 7](https://github.com/ucl-comp0035/comp0034-cw1-g-group-7-1.git)

### Set-up Instructions

Assuming that requirements will be installed from [requirements.txt](../requirements.txt), the full list is provided in that file.

All the requirements can be installed using the `pip install ...` method. The only additional requirement that is not in
the txt file is the *dash[testing]*. This can be installed by using the following code and running it in the terminal
within the venv: `pip install dash[testing]`.

The requirements added to the txt file that were not previously installed are also listed below:

- plotly
- pytest-cov
- selenium
- numpy

## Design of the app

Considering the data set available, the team decided to investigate and come up with some specifications about the
target audience and the possible questions to be answered. Before the start of the project the team decided that they
would have focused on different area in order to spam over a wider range of possible questions and target audience. For
this reason the goal or massive transformative purpose (MTP) of the team was to produce an interactive, user-friendly
app that would have enabled user from different backgrounds to efficiently obtain truthful information about starting a
business. The investigation process needed to identify and produce the target audience and questions was considered of
paramount importance due to its influence on the design of the app. In the next few sections a more detailed outline of
the targeted audience and the chosen questions to be answered is presented before outlining the design itself.

### Target Audience

The soon-to-be developed web-based app, will have the characteristics of an interactive dashboard and will be accessible
to everyone. However, during the kick-off of the project, the Inspire Future Potential (IFP) team has identified three
different possible groups of target audience. Considering the information that will be provided on the app, the first
group of target audience can be identified in the potential entrepreneurs wanting to start a business. However, as
mentioned before, the team also wanted to expand the target audience of the app. Thus, they hope that the app will be
used by local administrative authorities to help them realize the possible areas of improvement to increase
entrepreneurial attractiveness. Finally, as the app will be accessible to anyone, the team expects it to become a
benchmark for students or professionals interested in the research field. Considering the three groups of target
audience, three different personas have been developed.

#### Persona 1: Potential Entrepreneurs

![Persona 1.png](../Images/Persona1.png)

#### Persona 2: Administrative Authorities

![Persona 2.png](../Images/Persona2.png)

#### Persona 3: Researchers

![Persona 3.png](../Images/Persona3.png)

### Questions to be answered with the app

Considering the target audience previously defined, and the overall goal set by the team, the following questions should
be answered when using the app. The main question to be answered would be:

- Which country represents the best option to start a business in terms of costs, time and procedures required?

Along with the main question, there are multiple subquestions that are more specific:

- What is the relation between income group and starting a business score?
- How have the costs, time and procedures required for starting a business changed over time with respect to gender and
  geographical region?
- How does gender impact indicators' scores in different countries?
- What differences and similarities can be found between countries in different years based on gender?
- Which is the geographical region that offers the best options for starting a business?
- Which countries share similar scores for different starting business indicators?
- What differences can be found between indicators for countries in specific geographical regions?

While the main question is of interest for every group of target audience, the subquestions are more specific to some
groups. For example, a local administrator would be interested in making a comparison between his country and a foreign
one; while a researcher may be more interested in observing changes over time and impact of different indicators.

### Data Set

The data that will be examined and used to create the visualisation web app were taken from the World Bank Group,
[Doing Business project](http://www.doingbusiness.org/). The data were downloaded and prepared in a previous part of the
project resulting in the *DBJoint.csv* file. However, considering that different charts requires different structures of
the data set, further data manipulation was performed. Pandas library was used to generate different sub data set to
produce the visualisations and the file can be found in the data set folder.

### App overall design

Before analysing in more depth the different app pages and visualisation produced, an outlook of the overall structure
of the app is necessary. When developing the design for the overall web app structure, the team decided to first perform
some research on what are considered good web design principles [1,2]. Moreover, the team decided to also browse through
web app with similar purposes to understand key patterns and functionalities. After conducting a preliminary research
the team came up with a list of principles to guide them through the web app design. The five principles are outlined
below and explained in further details in the next sections.

List of good web app design principles:

- Website purpose
- Navigation and reading patterns
- Visual hierarchy
- Simplicity and consistency
- Establish credibility

Based on the aforementioned principles, the team decided to design an app that would have accommodated the needs of the
user by having a simple clear intention on every page (website purpose principle). This resulted in a multi page app
where every page has a clear purpose that is outlined in the main page together with other information. Having a multi
page design however requires an easy navigation, which is key to retaining users. This is because a user needs to be
able to quickly understand where to look for specific information and hence the navigation bar was made intuitive and
simple. Moreover, every page was designed to follow the users' natural pattern of scanning the page. This was found to
be either F-shaped or Z-shaped depending on the length of the page (navigation and reading patterns principles). In
order to facilitate readability and establish focal points a visual hierarchy was also established. This was implemented
by using different sizes (titles, subtitles etc), colours and contrast (visual hierarchy principle).

In addition, every page in the multi pages needs to be consistent and simple. To assure consistency, the team decided to
establish a simple design patterns with filters on the top and using a grid layout. Moreover, the team also chose to
leave the graphic design aspect to the end, after having put all the pages together, to assure consistency. Finally, the
team wanted to establish credibility. This was considered vital due to the data and purpose of the app; for this reason
the team decided to integrate an about us page.

The overall design of the web app is therefore that of a multi page app that allows easy navigation through different
pages, each having a precise and intuitive purpose to allow the best possible experience.

## Software Engineering and Data Science Tools & Techniques

The team decided to apply software engineering practices to organise their work. In particular the team tried to combine
the short development cycles of extreme programming (due to the limited time frame for the realization of the project),
with scrum's recurring meetings to organise, plan and revise the work. The meetings were recorded using a weekly minutes
file for status reporting. The Timeboxing and MoSCoW techniques of the Dynamic systems development method will also be
used. The former will allow focusing mainly on high priority project portions based on deadlines or business relevance.
The latter will instead provide a technique for prioritising requirements during the development of the web-based
visualization app. Moreover, throughout the whole project the team will also try and create components that could be
reusable in other projects, which is one of the main principles of the Data Science Life Cycle method. Finally,
considering the level of inexperience of the team members, Kanban's principle of no team roles was also applied.
**Lista di ref da vecchio (3-data science life cycle, 6-kanban, 1-xp, 4,8 - scrum)**

Considering the nature of the project and size of the team (4 people), it was necessary to use a source code control
system. The team decided to use GitHub due to general availability and previous experience. However, since the team
members have always used GitHub individually, before starting to work in a team, every member had to read a guide [3].
The team decided to use GitHub by creating one branch per member and generating pull requests to merge changes approved
during team meetings into the master branch. All pull requests had to be compared, reviewed and accepted by another
member of the team. For both pull requests and issues, the team decided to always use the assign and labels features and
add appropriate comments to keep clear track of the changes. Moreover, in order to have the best continuity between
meetings and project changes a webhook was created. This was needed to integrate Microsoft Teams (where the meetings
were held) and GitHub. The integration was set up to notify members in case of pull requests, merges, branch creation
and deletion and discussions or issues (example in the image below).

![Integration with teams.png](../Images/webhook.png)

In order to control the accuracy and style of the code, and also for consistency between team members, everyone had to
integrate the use of linters (PEP8). Moreover, some general guidelines regarding variable names, functions structure and
commenting were outlined at the beginning of the project. Finally, continuous integration was set up using GitHub
actions, once the testing stage was reached. This has proven extremely helpful in order to identify limitations in 
using selenium and dash testing for a multi page app. 
