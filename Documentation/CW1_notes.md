# Coursework 1 Notebook

## Target Audience

The soon-to-be developed web-based app, will have the characteristics of an interactive dashboard and will be accessible
to everyone. However, during the kick-off of the project, the IFP team has identified three different possible groups of
target audience. Considering the information that will be provided on the app, the first group of target audience can be
identified in the potential entrepreneurs wanting to start a business. However, as mentioned before, the team also hopes
that the app will be used by local administrative authorities to help them realize the possible areas of improvement to
increase entrepreneurial attractiveness. Finally, as the app will be accessible to anyone, the team expects it to become
a benchmark for students or professionals interested in the research field. Considering the three groups of target
audience, three different personas have been developed.

#### Persona 1: Potential Entrepreneurs

![Persona 1.png](../Images/Persona1.png)

#### Persona 2: Administrative Authorities

![Persona 2.png](../Images/Persona2.png)

#### Persona 3: Researchers

![Persona 3.png](../Images/Persona3.png)

## Questions to be answered using the dataset

Considering the problem statement and the target audience previously defined, the following questions should be answered
using the dataset. The main question to be answered would be:

- Which country represents the best option to start a business in terms of costs, time and procedures required?

Along with the main question, there are multiple subquestions that are more specific:

- What is the relation between income group and starting a business score?
- How have the costs, time and procedures required for starting a business changed over time with respect to gender and
  geographical region?
- Which is the geographical region that offers the best options for starting a business?
- Which countries share similar scores for different starting business indicators?
- How many countries have had more than 50% reduction in one or more indicators' values?
- What differences can be found between indicators for countries in specific geographical regions?

While the main question is of interest for every group of target audience, the subquestions are more specific to some
groups. For example, the last one could be of interest for the target audience groups represented by the personas 2 and

3. On the other hand, the third question could be of interest for an entrepreneur (persona 1).

## Ideas for charts

### Andrea

Considering the data and the questions to be answered me and Cate came up with a few ideas.

Focusing on the main question to be answered what could be useful is to have a choropleth map
[https://datavizcatalogue.com/methods/choropleth.html](https://datavizcatalogue.com/methods/choropleth.html). However
instead of being a normal map we can make it more interactive by implementing a zoom-in approach. What I mean is to
create something that goes from general to specific gradually. More specifically it would be a choropleth map of the
whole world, however considering that there are 191 countries it could be messy and misleading to show them all on the
same map. This could cause something like overcrowded data resulting in hiding some and counterproductive (having some
countries much bigger than others in terms of area, people would hover and focus on those rather than looking at smaller
countries as well for example). Therefore, since these countries are split in 7 geographical regions, it could be useful
to show a map of the world divided only for those 7 regions. The data that will be displayed or the legend will be based
on the overall starting a business score. This will be calculated for each region by averaging the one of the singular
countries. However, something more could be implemented such as the hovering function. This mean that when hovering over
a region
(example: europe) more data appear such as the score for cost, time and num of procedures (these are the indicator that
make up for the overall score). Finally, when clicking on a specific region what would happen is that it would zoom in
and at this point the singular countries for that region would be shown with their own values. Moreover, some countries
have values for also different cities that can be shown by putting a circle or dot in the geographical position. Look at
the very approximate sketch shown below.

![Sketch Choropleth.png](../Images/Sketch_choropleth.png)

Considering other questions the following charts could also be implemented:

- Radar
  chart [https://datavizcatalogue.com/methods/radar_chart.html](https://datavizcatalogue.com/methods/radar_chart.html)
  used to show for each geographical region or country the different score values for the indicators. This kind of shows
  the 'performance' of that region/country in specific
- Bar chart [https://datavizcatalogue.com/methods/bar_chart.html](https://datavizcatalogue.com/methods/bar_chart.html)
  this can be used to show for a singular indicator all the countries or region values. Imagine for example that it
  could be used to show in a sort of way the ranking so from the highest score or value to lowest. Again this can be
  implemented with a generic to specific approach (region -> countries of selected region) making it more interactive
- Classic line chart to show progression over time of a certain indicator maybe, reference to
  [Upper_middle_income.png](../Previous meterial/Upper_middle_income.png),
  [Score_regional_analysis.png](../Previous meterial/Score_regional_analysis.png),
  [Lower_middle_income.png](../Previous meterial/Lower_middle_income.png),
  [low_income.png](../Previous meterial/low_income.png),
  [High_income.png](../Previous meterial/High_income.png)

Finally, a bubble
chart. [https://datavizcatalogue.com/methods/bubble_chart.html](https://datavizcatalogue.com/methods/bubble_chart.html).
This can be used to show the relation between 3 variable: how cost depends on value of num of procedure and time. If you
look at the TED talk video he uses it in the way from generic to specific. So plotting bubbles for geographical regions
and if you click on them, they open up in the different country bubbles. Moreover, we could plot 1 bubble for the value
for male and one for the value for female generating a 4/5 variable chart (time vs num of procedure vs cost for male vs
female in diff countries)