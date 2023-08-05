### Application Name

**Remembering**

### Application Manifesto

<!--
Short one-sentence description of the application
-->

Remembering what's important

-> Forming habits?

### Application Goals

<!--
See also: Personas -> User goals
-->

* Remembering to *think* about things
    * *Gratitude*
    * Giving the user positive energy (maybe through images)
    * Helping the user remember those dear to her (photos)
    * Remembering wisdom quotes (or short texts). Ex: Remembering death
* Remembering to *do* things - PLEASE NOTE: This takes more time and mental energy and we may want this in a different
  application, or separate in another way
    * Starting a software application. Ex: Diary application
    * Visiting a website. Ex: Social media
    * Doing something at the computer. Ex:
    * Doing something away from the computer. Ex:
* Storing valuable *wisdom*
    * Storing quotes
    * Storing poetry
    * (Tags can be used to find it more easily)

Examples of types of entries:

* From diary
* Quotes that the user has found
* Personal affirmations
* Gathas (for breathing with)
* Family photos
* Gratitudes from the past (from the diary)
* Gratitude for things in the present (that are there all the time like food, etc)
* Practices?
* Breathing
* Mindfulness sliders*

### Personas

<!--
For each user persona:
* State of mind
* Needs
* Goals (when using the application)
* Environments (when and where will the user will be when using the application)
* Behaviour patterns
* (Skills and attitudes)
-->

#### Persona 1

Mental formations:

* Anxiety
* *Disconnection* from family, friends, nature, and the world

Needs:

* Connection
    * Friendship (including family)
* Wisdom/Insight
* Energy, support

Goals:

* Remembering the face of a loved one
* Remembering an inspiring quote
* Action: Remembering to post a photo on social media
* Understanding something about suffering (keeping this in mind, even though it's unpleasant)
* Action: Remembering to close the computer at a specific time

Equipment:

* User has a stationary computer, a laptop and a mobile phone
* User spends a lot of time at the computer, both working and relaxing
* User doesn't want to check notifications when out with the mobile???

Usage:

Situation | When | Where
---|---|---
User lets the application run in the background | 18-22 | on a laptop computer
User starts the application and closes it again after checking the notifications | 20 | -

Behaviour patterns:

* User is anxious, and quickly switches between different things

#### Persona 2

At work

### Scenarios

<!--
> A scenario created in the UCD process is a fictional story about the "daily life of" or a sequence of events with the primary stakeholder group as the main character.

UCD book:
> Scenarios are mini stories that reflect situations the user may find themselves in

> Scenarios, just like scenes in a movie, are specific situations that the user might find herself in. Using scenarios you can explore how the application will respond (or not respond) to the users needs

Addition by me: Scenarios can ask questions that are useful for thinking about how the application can help the user in that specific situation

UCD book: Scenarios are a way to reach the goal (user goal?)
-->

Including the situation (when and where) the application is used

Situation | Question of the application
---|---
The user is at home and has a low amount of energy | How can the appl remind her of the goodness in herself, her interconnection with others, and the world?
User is at the computer and wants to get some positive input | How can the appl help her find things that will boost her mood?
The user has had delusional/ignorant thinking about herself and the world | How can the appl help the user remember the wisdom she has read in books?
User hasn't been in touch with a friend for a long time | How can the appl help her remember to call her friend?
User has been using the computer for a long time and can benefit from closing the computer for the day | How does the application remind her of this? And how can the user delay the notification for a while?

### Use cases

<!--
#In short, a use case describes the interaction between an individual and the rest of the world."
-->

Actor | World
---|---
User starts the application @home 19:00 | -
- | Notifications set for the afternoon are shown
User clicks on one with a quote | -

Actor | World
---|---
User clicks on an action-related notification entry | -

Actor | World
---|---
User clicks on a thinking-related notification entry | -

Actor | World
---|---
User clicks on an action-related static entry | -

Actor | World
---|---
User clicks on a thinking-related static entry | -

Actor | World
---|---
User clicks on an action-related notification tag | -
- | Random action comes up (this can be useful for self-care)

Actor | World
---|---
User clicks on a thinking-related notification tag | -
- | Random

Actor | World
---|---
User clicks on an action-related static tag | -

Actor | World
---|---
User clicks on a thinking-related static tag | -

Actor | World
---|---
User finds a new quote she wants to add | -
User starts the application @19:30 | -
- | Appl shows missed notifications
User adds the quote to the appl. | -
User choses the notification time for the quote | -

Remembering a quote from a book (or Buddhist Sutra)

User remembers a dear friend, a pet, family member, or inspiring person

### User reqs

<!--
Adding example as a header here?
-->

Requirement | Description | Priority
---|---|---
Templates for text | Ex: for friends with (A) needs, (B) contact info (clickable??) | Medium
Tags | Ex: gratitude (energy, friends, family, inspiring people, ), impermanence (death, ), inter-being. Show in taskbar or not (checkbox) | High
Needs as tags | is this standard tags? something else? or "need:friendship" | ???
Short texts | | Essential
Long texts | | Medium
Image | | Essential
Breathing | | Low?
Notifications for entries | - | Essential
Notifications for tags | - | Medium?
Website | Could be combined with "custom runnable" | Low
Custom "runnable" | | Low?
*Entering* pre-chosen text | mbed idea. Two-way | ???
Todo with checkbox | Two-way. Combine with "not fired"? | Low?
Static content items | Can be used for if-then situations | Low???

#### User-experience goals ("soft requirements")

* The appl can be run in the background or started just now and then
* The application *gently* reminds the user
* The application gives support for the user to *stay and rest* with a single content (for example quote)
    * (Maybe with calm music, breathing, or something else)
* **When the user connects with (likes) something it's important that she can see more of this** (can be achieved using
  tags for example)

### Scope

#### Limitation

Excluded | Reason | Other applications
---|---|---
Application checking in with the user | This may get lost in the amount of notifications | A new application maybe. Or MatC with sliders
Breathing??? | We could call maybe MatC with a string describing what breathing phrase we want?
Storing vast amounts of quotes. We only store things we want to remember | We don't want the user to become a hoarder | Text files?
If-then | |
Static | |

#### When the user is open and opened

-

#### Relation with other applications

##### MatC

Breathing dialog

##### Well-Being Diary

Can be opened once per day from Remembering

#### Platforms

Platform | Fit
---|---
Desktop | Works well

Web
Mobile


***

### Psychological perspectives

Perspectives/Views

Emotional / Getting energy

#### Buddhist Perspective

N8P: Right view, (right intention and effort)

Right Intention, Speech, Action

#### NVC Perspective

Needs (Needs as tags?)


***

### Usage situations

* Running in the background
* Starting once per day, and then closing after viewing notifications
* Starting a few times per week (and closing again)

### Design considerations

<!--
Based on the above, what are some design considerations important to keep in mind?
-->

Actions and thinking:

* Thinking first?
*

"We only store things we want to remember":

* Requiring notification time? Otherwise tags can be used though
* Automatically remove old entries?

In the wider context of well-being applications on desktop computers this is the only application that will run in the
background with the purpose of reminding the user to open other applications. Therefore it's the most important
application to have on auto-start

Randomized content for tag?

Time: presets (evening, etc), or hours on a slider

Full-screen view & smaller view

edit button in full-screen view for easy editing

"not fired" button in the fs view (so the user can see the same item again)

order for items in fs view?
Different types of entries, or different elements "inline"?

TODO: Is there a checkbox?

Checkbox for all content: "Taking it in" OR "Doing" ("actions", "thinking")

* Automatically checked after x seconds, or after clicking on "open website" (or similar)

### GUI

Full-screen view:

* Removing future notifications
* Done

Systray menu:

* Entries `entry` {content}
    * Static entries `[in brackets]`
*
    - (separator)
* Tags `#hashtag` {random content}
    * Static tags `[#in-brackets]`
* (Also the content can be action-oriented or thinking-oriented)

Main window list:

* ~~Active~~
* Time until next notification
*

Main window details:

* Notification time
* Content
*

### Db design

* Content type
    * Image
    * Text
    * Website
    * Advanced
        * File (using custom open action)
        * Custom
        * ~~Breathing~~
* Action/thinking type:
    * Action
    * Thinking
* Ordering
* Content
* "Taking in" time
    * 0 means that there is only "manual done"


* Notifications
    * Mo-Su
* Tags

What happens if something isn't done?



