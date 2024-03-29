This repository is archived and read only.

If you want to unarchive it, then post to the [Admin & Infrastructure (AI) Team category on the Plone Community Forum](https://community.plone.org/c/aiteam/55).

Introduction
============

This addon package jscalendar_ for Plone

Version: 1.0

About jscalendar
================

This is Mihai Bazon's <mihai_bazon@yahoo.com> excellent DHTML Calendar
Widget, ("jscalendar") available in original from:
http://dynarch.com/mishoo/calendar/old


For version 1.0 of jscalendar, included in Plone 2.1, the
integration from the previous jscalendar versions was changed
slightly.

For distribution with Plone, we have flattened the directory
hierarchy, added this file (README-Plone), added all of the .metadata
files and applied the patch at the end of this file. Everything else
is unchanged. This means the subdirectories "doc", "doc/html", "skins",
"skins/aqua" and "lang" have been removed, with their contents
moved to the top jscalendar directory instead. This is only in order to
 avoid making "doc", "doc/html", "skins", "skins/aqua" and "lang"
available from other url's on a site, due to Zope's acquisition logic.

Upgrading Plone's jscalendar
----------------------------

When a new upstream version is available it should be simple to
integrate it with Plone. Just flatten its directory hierarchy and run
"diff -ru jscalendar jscalendar-x.y.x", to see if there are any
changes that might be significant to the Plone integration. Pay close
attention to calendar-setup.js. Any changes there might have to be
reflected in calendar_formfield.js. Also apply the code changes 
listed at the end of this file.


Plone integration
-----------------

- i18n

  jscalendar uses its own translations, i.e. not plone-i18n. The
  jscalendar translations are available in the various calendar-*js
  files. 

- skins

  jscalendar comes with several default skins. The default skin is
  calendar-system.css, which uses standard CSS features to make the calendar
  look similar to other user interface components of the operating system that
  the web browser is running on.

- references in Plone files:

  calendar_formfield.js
      - function showJsCalendar (mimics Calendar.setup() as an ordinary
        function instead of as a handler)
      - function update_date_field

- other

  calendar-setup*.js isn't used by the Plone integration (it would require
  adding a little javascript after the </form> tag, which seems
  difficult to do with CMFFormController, as the script still needs to
  refer to the controls by id. Added .metadata files for it anyway.

- code changes

    - add a vertical offset of 2, so the calendar doesn't obscure (and
      then autohide) the other date/time controls.

      Change:
        this.showAt(p.x, p.y + el.offsetHeight);
      To:
        this.showAt(p.x, p.y + el.offsetHeight + 2);

    - Add a style definition to all style sheets. This closes issue 1628,
      http://plone.org/collector/1628. This is due to line 1228 of the
      plone.css stylesheet, which changes the layout for all label
      elements to be inline. Removing the line "display: inline" is how
      this problem will probably be fixed for later Plone versions, as it
      seems to be unneeded (no negative effects could be found). It is
      however too late in the release cycle to risk breaking something
      else. The preferred plone.css fix in future Plone versions:

        .label {
            font-weight: bold;
            /* display: inline; */
            padding-right: 0.5em;
        }

      In all *.css files change:

      .calendar .combo .label,
      .calendar .combo .label-IEfix {
        text-align: center;
        padding: 1px;
      }

      To:

      .calendar .combo .label,
      .calendar .combo .label-IEfix {
        text-align: center;
        display: block;
        padding: 1px;
      }
