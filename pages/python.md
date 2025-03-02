---
title: "קורס פייתון"
timestamp: 2019-11-07T07:30:01
tags:
  - Python
published: true
books:
  - python
author: szabgab
archive: true
show_related: false
---


זאת ההתחלה של קורס פייתון המבוסס על [השקפים](https://code-maven.com/slides/python/).

ההמשך יבוא.

רשימת הסרטונים נמצאת בצד שמאל של דף זה ובכל דף ששייך לסדרה.

אתם גם מוזמנים להשתמש בחצים Next וPrev.


* [מבוא](/python-programming)
    * [תכנות פייתון](/python-programming)
    * [מה זה תכנות?](/python-what-is)
    * [התקנת פייתון](/python-installing)
    * [סביבות פיתוח לפייתון](/python-editors-and-ide)
    * [דוקומנטציה של פייתון, קבלת עזרה בפייתון](/python-documentation)
    * [סוגי תוכנות](/python-program-types)
    * [תוכנה ראשונה בפייתון: שלום עולם](/python-hello-world)
    * [next](/python-comments)
    * [next](/python-variables)
    * [next](/python-exercise-hello-world)
    * [next](/python-what-is-programming)
    * [next](/python-what-are-programming-languages)
    * [next](/python-value-types)
    * [next](/python-numerical-operations)
    * [next](/python-exercise-calculations)
    * [next](/python-solution-calculations)

* [מבוא פרק 2](/python-modules)
* [מספרים](/python-numbers)
* [בולאנים](/python-boolean-operators)
* [מחרוזות](/python-strings)
* [לולאות](/python-loops)
* [ מחרוזות הדפסות מפורמטות](/python-formatted-strings)
* רשימות
* קבצים
* מילונים
* סטים
* פונקציות
* מודולים
* אריזות
* [ביטויים רגולרים](/python-what-are-regexes)
* מודולים סטנדרטים
* ישון
* פרמטרים בשורת הפקודות
* [שגיאות](/python-exception-handling-hierarchy-of-calls)
* [תיכנות מונחה עצמים](/python-oop-what-is-oop)
* [תרגילי תכנות מונחה עצמים](https://code-maven.com/slides/python/exercise-oop-move)

<!--
## רשימות

    <li><a href=""></a></li>

<ol>
    <li>יצירת רשימה</li>
    <li>שליפת ערך מרשימה</li>
    <li>עדכון ערך ברשימה</li>
    <li>גישה לחתך של רשימה</li>
    <li>השמה והעתקה של רשימות</li>
    <li>האם ערך נמצה ברשימה?</li>
    <li>הוספת ערך באמצע הרשימה</li>
    <li>הוספת ערך בסוף הרשימה</li>
    <li>שליפת ערך מרשימה</li>
    <li>מעבר על כל הערכים של רשימה</li>
    <li>מעבר על האינדקסים של הרשימה</li>
    <li>תור</li>
    <li>מחסנית</li>
    <li>מיון רשימות</li>
    <li>מיון רשימה לפי ערך אחר</li>
    <li>טווחים (range)</li>
</ol>

## קבצים

<ol>
    <li>פתיחת קובץ לקריאה</li>
    <li>שם קובץ בשורת הפקודות</li>
    <li>קובץ שלא קיים</li>
    <li>טיפול בשגיאות בעת פתיחת קובץ וקריאה ממנו</li>
    <li>מעבר על מספר קבצים</li>
    <li>יצירת קובץ וכתיבה לקובץ</li>
    <li>הוספת שורות לקובץ קיים</li>
    <li>קבצים בינאריים</li>
    <li>בדיקה האם קובץ קיים</li>
</ol>

## מילון

<ol>
    <li>מה זה מילון בפייתון, לאיזו מטרה משתמשים במילון?</li>
    <li>יצירת מילון</li>
    <li>גישה לערכים במילון</li>
    <li>מעבר על כל המפתחות במילון</li>
    <li>בדיקת קיום של מפתח</li>
    <li>מחיקת מפתח ממילון</li>
    <li>רשימה של מילונים</li>
</ol>

## סטים

<ol>
    <li>פעולות על סטים</li>
</ol>

## פונקציות

<ol>
    <li>למה להשתמש בפונקציות</li>
    <li>הגדרת פונקציה פשוטה</li>
    <li>פרמטרים לפי מיקום</li>
    <li>פרמטרים לפי שם</li>
    <li>ברירת מחדל לערכים</li>
    <li>מספר לא מוגדר של פרמטרים</li>
    <li>זוגות של מפתח-ערך נוספים ברשימת הפרמטרים</li>
    <li>הגדרה כפולה של אותו שם לפונקציות ובכלל</li>
    <li>פונקציות רקורסיביות</li>
    <li>פונקצית פיבונצי</li>
    <li>דוקומנטציה של פונקציות</li>
</ol>

## מודולים

<ol>
    <li>מעבר משימוש בפונקציה בקובץ שבו היא מוגדרת לפונקציה שמוגדרת בקובץ אחר</li>
    <li>איך פייתון מוצא את הקובץ המתאים?</li>
    <li>דרכים שונות לשנות את רשימת המקומות בהם פייתון מחפש מודולים</li>
    <li>מסלול רלטיבי</li>
    <li>מסלול אבסולותי</li>
    <li>קומפילציה של מודולים</li>
    <li>יבוא מודולים בזמן ריצה</li>
    <li>יבוא מודולים לפי תנאים מסוימים</li>
    <li>מודול או סקריפת להרצה?</li>
    <li>האני של פייתון</li>
    <li>דוקטסט</li>
</ol>


## ביטויים רגולרים

<ol>
    <li>רגקסים</li>
    <li>התאמה של מספרים</li>
    <li>תפיסת מחרוזות</li>
    <li>מציאת כל המופעים</li>
    <li>תו כלשהו</li>
    <li>קבוצות של תווים</li>
    <li>קבוצות ידועות של תווים</li>
    <li>שלילה של קבוצת תווים</li>
    <li>תו אופציונלי - המכמת הראשון</li>
    <li>מכמתים</li>
    <li>התאמת מספרי ISBN</li>
    <li>התאמה לחלק של מחרוזת עם סימני תחילה וסוף</li>
<ol>

-->
