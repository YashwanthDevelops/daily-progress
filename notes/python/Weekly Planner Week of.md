# 📅 Weekly Planner – [Week of __/__/__]

## 📊 Overview
> This master board gives you a one‑page snapshot of the entire week.  
> Click a day to drill down into the Daily Scheduler.

| Day | DSA Target | Skill Hours | Gym | Class Load | ⏱ Time |
|-----|------------|-------------|-----|------------|--------|
| **Sunday** | 2 | 1–2 | Rest/Walk | HOLIDAY | 08:00‑22:00 |
| **Monday** | 3 | 5+ | Push | HOLIDAY | 06:45‑23:00 |
| **Tuesday** | 2–3 | 3+ | Pull | Light | 06:45‑23:00 |
| **Wednesday** | 2–3 | 3.5+ | Legs | Medium | 06:45‑23:00 |
| **Thursday** | 2–3 | 2.5+ | Push | Medium | 06:45‑23:00 |
| **Friday** | 1–2 | 1 (opt) | — | HEAVY | 06:45‑23:00 |
| **Saturday** | 3 | 2+ | Pull | Medium | 06:45‑23:00 |

> **⚙️ Customise** the “Time” column if your actual class schedule differs.

---

## 🗓 Daily Scheduler

> Each row is a **time‑block**.  
> The “Duration” column is auto‑calculated (end – start).  
> Use the checkbox to mark completion.

| Time | Block | Activity | Notes | ✅ |
|------|-------|----------|-------|----|
| 06:45 | Wake‑up |  |  |  |
| 07:00 | DSA #1 |  |  |  |
| 07:45 | Break |  |  |  |
| 08:00 | Skill Block |  |  |  |
| 09:00 | Breakfast |  |  |  |
| 09:30 | Walk to class |  |  |  |
| 10:00 | Class |  |  |  |
| 13:20 | Lunch |  |  |  |
| 14:00 | Walk to class |  |  |  |
| 14:10 | Class |  |  |  |
| 16:40 | Return |  |  |  |
| 17:00 | Snack |  |  |  |
| 17:30 | DSA #2 |  |  |  |
| 18:30 | Gym / Walk |  |  |  |
| 19:00 | Break |  |  |  |
| 19:30 | Academic Review |  |  |  |
| 20:00 | Dinner |  |  |  |
| 20:30 | Parent Call |  |  |  |
| 21:00 | Friend Call |  |  |  |
| 21:15 | Light Work |  |  |  |
| 22:00 | LinkedIn/Twitter |  |  |  |
| 22:30 | Night Routine |  |  |  |
| 23:00 | Sleep |  |  |  |

> **Tip:** Drag rows to reorder if you prefer a different flow for a given week.

---

## 📚 DSA Tracker

> Use this database to log every LeetCode/Notion problem you solve.  
> Click **+ New** to add an entry.

| Date | Problem ID | Difficulty | Category | Notes | ✅ |
|------|------------|------------|----------|-------|----|

> **Filters**:  
> • `Date` within current week.  
> • `✅` unchecked for pending problems.

---

## 🏋️‍♂️ Gym Log

> Track workout type, duration, and any notes.

| Date | Workout | Duration | Notes | ✅ |
|------|---------|----------|-------|----|

> **Board View** (by Workout) lets you see how many sessions of each type you did.

---

## ⏱ Skill Hours Log

> Record the time spent on each skill‑building activity.

| Date | Activity | Duration (hrs) | Notes | ✅ |
|------|----------|----------------|-------|----|

> **Rollup** in the Weekly Dashboard will sum the `Duration (hrs)` column.

---

## 📈 Weekly Metrics Dashboard

> Automatic calculations to compare your actual performance against targets.

| Metric | Target | Actual |
|--------|--------|--------|
| **DSA Problems** | 15+ | `sum(DSA Tracker | ✅ unchecked)` |
| **Skill Hours** | 18+ | `sum(Skill Hours Log | Duration (hrs))` |
| **Gym Sessions** | 5–6 | `count(Gym Log)` |
| **Sleep Before 11:15 PM** | 6/7 days | `count(where Sleep time < 23:15)` |
| **Screen Time** | <3 hrs avg | `average(Screen Time Log | Duration)` |

> **How to set up formulas**  
> 1. Create a **Formula** column in each database (e.g., `Actual`).  
> 2. Use Notion’s roll‑up syntax: `rollup(DSA Tracker, ✅, count)` etc.  
> 3. Add a **Status** column that turns green when the target is met.

---

## 🔁 Recurring Actions Checklist

> Use this to set up your first day of the week (or any recurring task).

- [ ] Set all alarms for the week (6:45 AM).  
- [ ] Turn off notifications during deep‑work blocks.  
- [ ] Prepare gym clothes/bag the night before.  
- [ ] Screenshot the schedule for quick reference.  
- [ ] Buy protein if not already done.  

---

## 📑 Views & Filters

| Database | View | Purpose |
|----------|------|---------|
| Weekly Overview | Board (by Day) | Quick glance at each day. |
| Daily Scheduler | Calendar | See time blocks on a calendar. |
| DSA Tracker | List (by Date) | All problems solved this week. |
| Gym Log | Board (by Workout) | Visualise workout distribution. |
| Skill Hours Log | Calendar | See when you spent time on skills. |
| Metrics Dashboard | Table | Compare actual vs target. |

> **Tip:** Add a **"Today"** filter to each database to only show items relevant for the current day.

---

## 🎉 Done!

You now have a *single, integrated* Notion workspace that:

1. **Tracks your schedule** with time blocks.  
2. **Logs your learning** (DSA, skill hours).  
3. **Monitors your fitness** (gym sessions).  
4. **Shows your progress** against weekly targets.  
5. **Keeps recurring actions** in one place.  

Feel free to duplicate the page for each new week, adjust dates, or add new columns as your routine evolves. Happy planning! 🚀

---```

--- 

**How to import**

1. Open Notion → **+ New Page** → **Import** → **Markdown & CSV**.  
2. Paste the block above.  
3. Click **Import**.  
4. The page will open with all databases, tables, and views ready to use.  

Enjoy your *best‑in‑class* planner!

