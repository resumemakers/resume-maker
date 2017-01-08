Feature: Resume generation

    @basic
    Scenario: en basic
        When send a "example" json:
        """
        {
            "name": "George the Martian",
            "function": "Youtube senior analyst",
            "phone": "+55 287298121",
            "email": "George@martian.com",
            "address": "73 N. Oak Drive - Dyersburg, TN 38024",
            "education": [
                ["PhD in the streets - Harvard",
                 "2001"],

                ["PhD in python - PyCon",
                 "every year"]

            ],
            "experience": [
                ["Scroll Master",
                 "Mai 2003 - Jun 2007",
                 "Scroll the scroll of the mouse pretending to program"],

                ["Garbage collector",
                 "Jan 2000 - Mai 2003",
                 "Collecting garbage in other codes"]

            ],
            "skills": [
                ["Python", 5],
                ["Java", 2],
                ["C++", 4],
                ["JS", 1]
                ],

            "languages": [
                ["Elvish", "Fluent"],
                ["English", "Basic"]
                ]
        }

        """
        And set "en" lang "basic" template
        Then resume was generated at "tmp"

    @basic
    Scenario: pt basic
        When send a "example" json:
        """
        {
            "name": "George the Martian",
            "function": "Youtube senior analyst",
            "phone": "+55 287298121",
            "email": "George@martian.com",
            "address": "73 N. Oak Drive - Dyersburg, TN 38024",
            "education": [
                ["PhD in the streets - Harvard",
                 "2001"],

                ["PhD in python - PyCon",
                 "every year"]

            ],
            "experience": [
                ["Scroll Master",
                 "Mai 2003 - Jun 2007",
                 "Scroll the scroll of the mouse pretending to program"],

                ["Garbage collector",
                 "Jan 2000 - Mai 2003",
                 "Collecting garbage in other codes"]

            ],
            "skills": [
                ["Python", 5],
                ["Java", 2],
                ["C++", 4],
                ["JS", 1]
                ],

            "languages": [
                ["Elvish", "Fluent"],
                ["English", "Basic"]
                ]
        }

        """
        And set "pt" lang "basic" template
        Then resume was generated at "tmp"

    @basic
    Scenario: es basic
        When send a "example" json:
        """
        {
            "name": "George the Martian",
            "function": "Youtube senior analyst",
            "phone": "+55 287298121",
            "email": "George@martian.com",
            "address": "73 N. Oak Drive - Dyersburg, TN 38024",
            "education": [
                ["PhD in the streets - Harvard",
                 "2001"],

                ["PhD in python - PyCon",
                 "every year"]

            ],
            "experience": [
                ["Scroll Master",
                 "Mai 2003 - Jun 2007",
                 "Scroll the scroll of the mouse pretending to program"],

                ["Garbage collector",
                 "Jan 2000 - Mai 2003",
                 "Collecting garbage in other codes"]

            ],
            "skills": [
                ["Python", 5],
                ["Java", 2],
                ["C++", 4],
                ["JS", 1]
                ],

            "languages": [
                ["Elvish", "Fluent"],
                ["English", "Basic"]
                ]
        }

        """
        And set "es" lang "basic" template
        Then resume was generated at "tmp"

    @red
    Scenario: en red
        When send a "example" json:
        """
        {
            "name": "George the Martian",
            "function": "Youtube senior analyst",
            "phone": "+55 287298121",
            "email": "George@martian.com",
            "address": "73 N. Oak Drive - Dyersburg, TN 38024",
            "education": [
                ["PhD in the streets - Harvard",
                 "2001"],

                ["PhD in python - PyCon",
                 "every year"]

            ],
            "experience": [
                ["Scroll Master",
                 "Mai 2003 - Jun 2007",
                 "Scroll the scroll of the mouse pretending to program"],

                ["Garbage collector",
                 "Jan 2000 - Mai 2003",
                 "Collecting garbage in other codes"]

            ],
            "skills": [
                ["Python", 5],
                ["Java", 2],
                ["C++", 4],
                ["JS", 1]
                ],

            "languages": [
                ["Elvish", "Fluent"],
                ["English", "Basic"]
                ]
        }

        """
        And set "en" lang "red" template
        Then resume was generated at "tmp"

    @red
    Scenario: pt red
        When send a "example" json:
        """
        {
            "name": "George the Martian",
            "function": "Youtube senior analyst",
            "phone": "+55 287298121",
            "email": "George@martian.com",
            "address": "73 N. Oak Drive - Dyersburg, TN 38024",
            "education": [
                ["PhD in the streets - Harvard",
                 "2001"],

                ["PhD in python - PyCon",
                 "every year"]

            ],
            "experience": [
                ["Scroll Master",
                 "Mai 2003 - Jun 2007",
                 "Scroll the scroll of the mouse pretending to program"],

                ["Garbage collector",
                 "Jan 2000 - Mai 2003",
                 "Collecting garbage in other codes"]

            ],
            "skills": [
                ["Python", 5],
                ["Java", 2],
                ["C++", 4],
                ["JS", 1]
                ],

            "languages": [
                ["Elvish", "Fluent"],
                ["English", "Basic"]
                ]
        }

        """
        And set "pt" lang "red" template
        Then resume was generated at "tmp"
