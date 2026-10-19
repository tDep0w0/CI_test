# 🛠️ Build Your Own CI Pipeline: BUILD UMass Workshop

**Your goal:** write tests for a calculator, then write a GitHub Actions pipeline that runs those tests automatically on every push and pull request.

When you're done, a bug shouldn't be able to reach `main` without a red ❌.

---

## 📁 What's in this repo

```
.
├── .github/
│   └── workflows/
│       └── ci.yml       ← your pipeline, with 6 blanks to fill in
├── calculator.py        ← the code you're testing (don't edit it)
├── test_calculator.py   ← your tests: one sample is done, you write the rest
├── requirements.txt     ← libraries the project needs (pytest)
└── README.md            ← you are here
```

> `.github` starts with a dot, so it may be hidden in Finder/File Explorer. You'll see it in VS Code or with `ls -a`.

---

## ✅ Before you start

- [ ] Logged into GitHub
- [ ] `git --version` works in your terminal
- [ ] `python3 --version` shows 3.10 or higher
- [ ] Git can push to GitHub. If you've never set this up:
  ```bash
  # Mac:      brew install gh
  # Windows:  winget install GitHub.cli
  gh auth login     # GitHub.com → HTTPS → Login with a web browser
  ```

---

## Step 0: Get your own copy (5 min)

1. At the top of this page, click the green **Use this template** button → **Create a new repository**
2. Name it (e.g. `my-ci-pipeline`), set it to **Public**, and click **Create repository**
3. Clone **your** copy and create a branch:
   ```bash
   git clone https://github.com/<your-username>/my-ci-pipeline.git
   cd my-ci-pipeline
   git checkout -b my-pipeline
   ```
4. Set up Python and run the tests:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate          # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   pytest
   ```
   ✅ You should see **`1 passed`** (the sample test).

> 📝 Remember the last two commands you just ran. You'll need them in Step 2.

---

## Step 1: Write your tests (10 min)

### How to write a test

A test is a function that runs your code and **checks the answer**. Here's the sample from `test_calculator.py`:

```python
def test_add():
    assert add(2, 3) == 5          # normal case
    assert add(-2, -3) == -5       # negative numbers
    assert add(0, 0) == 0          # zero
```

**The rules:**

1. **The name must start with `test_`.** That's how pytest finds it. `check_add()` would be ignored.
2. **Call your code, then `assert` the answer.** `assert` means "this must be true." If it's false, the test fails.
3. **Test more than one case.** A single `assert` is easy to fool. For example, `add(2, 2) == 4` passes even if someone changes `+` to `*`.
4. **Testing for an error** works differently. If your code is _supposed_ to raise an error, wrap it in `pytest.raises`:
   ```python
   def test_something_bad():
       with pytest.raises(ValueError):
           function_that_should_fail()
   ```
   This test **passes** if the error is raised and **fails** if it isn't.

**Running tests:**

| Command            | What it does                                 |
| ------------------ | -------------------------------------------- |
| `pytest`           | Runs every test, short output                |
| `pytest -v`        | Shows each test by name with PASSED / FAILED |
| `pytest -k divide` | Runs only tests with "divide" in the name    |

When a test fails, pytest shows you exactly which `assert` broke and what the actual value was:

```
>       assert add(2, 3) == 5
E       assert -1 == 5
```

### Your task

Open `test_calculator.py` and write:

- [ ] `test_subtract()`
- [ ] `test_multiply()`
- [ ] `test_divide()`
- [ ] `test_divide_by_zero()`: `divide()` raises a `ValueError` when dividing by 0

Run `pytest -v` as you go. ✅ When you're done: **`5 passed`** (or more if you added extras).

### ⚠️ Make sure your tests can actually fail

A test that always passes is useless. Check yours:

1. In `calculator.py`, temporarily change `return a - b` to `return a + b`
2. Run `pytest`. `test_subtract` should **fail**
3. Change it back and run `pytest` again. Everything should **pass**

---

## Step 2: Build your pipeline (10 min)

### 2a. Open the workflow file

Open `.github/workflows/ci.yml`. It's already in the right place: GitHub **only** runs workflows inside `.github/workflows/`, just like in the slides. In your own projects, you'll create this folder yourself.

### 2b. Fill in the 6 blanks

Replace every `____` using the workflow syntax from the slides.

### 2c. Push and open a pull request

```bash
git add .
git commit -m "Add tests and CI pipeline"
git push -u origin my-pipeline
```

Then on GitHub:

1. Go to **your** repo and click the yellow **Compare & pull request** banner
2. Make sure the base branch is **`main`**
3. Click **Create pull request**

### 2d. Watch it run

Scroll down on your PR to the checks box. **CI / test** goes 🟡 (running), then ✅ (passed) in about 30–60 seconds. Don't see it yet? Wait 30 seconds and refresh the page.

To see the log, click the ✅ (or open the **Checks** tab at the top of your PR). You'll see every step: checkout → set up Python → install → run tests. Click a step to expand it.

✅ **Goal: a green check on your PR.** Don't merge it yet!

---

## Step 3: Protect `main` (3 min)

Right now, anyone could still click **Merge** on a PR with a red ❌. Let's make GitHub **block** merging until CI passes.

1. In **your** repo, go to **Settings → Branches → Add classic branch protection rule**
2. **Branch name pattern:** `main`
3. ☑ **Require a pull request before merging**
   - Uncheck **Require approvals** (there's no one to approve today)
4. ☑ **Require status checks to pass before merging**
   - In the search box, type **`test`** and select it (that's the job name from your `ci.yml`)
   - It only appears after CI has run at least once, which you just did in Step 2
5. ☑ **Do not allow bypassing the above settings** (otherwise you, as the owner, can still merge a red PR)
6. Click **Create**

---

## Step 4: Prove it works (5–10 min)

A pipeline is only useful if it catches bugs. Time to test it.

1. **Swap laptops** with your neighbor
2. On _their_ laptop, break **one** function in `calculator.py`. **Don't touch the tests.**
3. Push it:
   ```bash
   git commit -am "sneaky bug"
   git push
   ```
4. **Swap back** and watch your PR. It re-runs automatically.

| Result   | Meaning                      | What to do                                                                                                        |
| -------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| ❌ Red   | Your pipeline caught the bug | Notice the **Merge** button is blocked 🔒. Click the red ❌ to find which test failed. Fix the bug, push, and get green again |
| ✅ Green | The bug got past your tests  | Write a new test that catches it, push, and confirm it's red. Then fix the bug, push, and get green               |

---

## Step 5: Merge it 🚀

Once your PR is green, the **Merge pull request** button unlocks. Click it.

Your workflow also triggers on `push` to `main`, so the merge starts one more run. Open the **Actions** tab to see it under **CI**.

🎉 **Done!** Your repo now has a working CI pipeline **and** a protected `main` branch. Every future PR gets tested automatically, and nothing broken can be merged, just like your BUILD project should work.
