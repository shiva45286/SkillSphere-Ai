// =======================================
// SkillSphere AI JavaScript File
// =======================================

console.log("SkillSphere AI Loaded Successfully");

// =======================================
// Form Validation
// =======================================

function validateRegistrationForm() {

    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let confirmPassword =
        document.getElementById("confirm_password").value;

    if (
        name === "" ||
        email === "" ||
        password === ""
    ) {

        alert("Please fill all fields");
        return false;
    }

    if (password.length < 6) {

        alert(
            "Password must contain at least 6 characters"
        );

        return false;
    }

    if (password !== confirmPassword) {

        alert("Passwords do not match");
        return false;
    }

    return true;
}

// =======================================
// Login Validation
// =======================================

function validateLoginForm() {

    let email =
        document.getElementById("email").value;

    let password =
        document.getElementById("password").value;

    if (
        email === "" ||
        password === ""
    ) {

        alert("Enter Email and Password");
        return false;
    }

    return true;
}

// =======================================
// Skill Search Filter
// =======================================

function searchSkill() {

    let input =
        document.getElementById("skillSearch");

    let filter =
        input.value.toUpperCase();

    let ul =
        document.getElementById("skillList");

    let li =
        ul.getElementsByTagName("li");

    for (let i = 0; i < li.length; i++) {

        let text =
            li[i].textContent ||
            li[i].innerText;

        if (
            text.toUpperCase()
            .indexOf(filter) > -1
        ) {

            li[i].style.display = "";

        } else {

            li[i].style.display = "none";
        }
    }
}

// =======================================
// Skill Progress Bar
// =======================================

function updateProgressBar() {

    let progress =
        document.getElementById("progressBar");

    if (!progress) return;

    let value =
        progress.getAttribute("data-progress");

    progress.style.width = value + "%";

    progress.innerHTML = value + "%";
}

// =======================================
// Welcome Message
// =======================================

function welcomeUser(name) {

    if (name) {

        alert(
            "Welcome to SkillSphere AI, " +
            name +
            "!"
        );
    }
}

// =======================================
// Confirm Delete
// =======================================

function confirmDelete() {

    return confirm(
        "Are you sure you want to delete your account?"
    );
}

// =======================================
// Dark Mode Toggle
// =======================================

function toggleDarkMode() {

    document.body.classList.toggle(
        "dark-mode"
    );

    if (
        document.body.classList.contains(
            "dark-mode"
        )
    ) {

        localStorage.setItem(
            "theme",
            "dark"
        );

    } else {

        localStorage.setItem(
            "theme",
            "light"
        );
    }
}

// =======================================
// Load Saved Theme
// =======================================

window.onload = function () {

    let theme =
        localStorage.getItem("theme");

    if (theme === "dark") {

        document.body.classList.add(
            "dark-mode"
        );
    }

    updateProgressBar();
};

// =======================================
// Character Counter
// =======================================

function countCharacters() {

    let text =
        document.getElementById("skills");

    let counter =
        document.getElementById(
            "charCount"
        );

    if (!text || !counter) return;

    counter.innerHTML =
        text.value.length +
        " characters";
}

// =======================================
// Email Validation
// =======================================

function validateEmail(email) {

    let regex =
        /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    return regex.test(email);
}

// =======================================
// Profile Form Validation
// =======================================

function validateProfile() {

    let skills =
        document.getElementById("skills")
        .value;

    let interests =
        document.getElementById("interests")
        .value;

    if (
        skills.trim() === "" ||
        interests.trim() === ""
    ) {

        alert(
            "Please enter skills and interests"
        );

        return false;
    }

    return true;
}

// =======================================
// Current Date
// =======================================

function showCurrentDate() {

    let dateElement =
        document.getElementById(
            "currentDate"
        );

    if (!dateElement) return;

    let today =
        new Date();

    dateElement.innerHTML =
        today.toDateString();
}

// =======================================
// Dashboard Statistics
// =======================================

function animateCounter(
    id,
    target
) {

    let count = 0;

    let element =
        document.getElementById(id);

    if (!element) return;

    let interval =
        setInterval(function () {

            count++;

            element.innerHTML = count;

            if (count >= target) {

                clearInterval(interval);
            }

        }, 20);
}

// =======================================
// Run Dashboard Functions
// =======================================

document.addEventListener(
    "DOMContentLoaded",
    function () {

        showCurrentDate();

        animateCounter(
            "skillsCount",
            10
        );

        animateCounter(
            "courseCount",
            20
        );
    }
);

// =======================================
// Course Recommendation Alert
// =======================================

function showRecommendation() {

    alert(
        "New AI Recommendations Generated!"
    );
}

// =======================================
// Logout Confirmation
// =======================================

function confirmLogout() {

    return confirm(
        "Do you want to logout?"
    );
}

// =======================================
// Scroll To Top Button
// =======================================

function scrollToTop() {

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}

// =======================================
// Auto Hide Flash Messages
// =======================================

setTimeout(function () {

    let flashMessages =
        document.querySelectorAll(
            ".flash-message"
        );

    flashMessages.forEach(function (
        message
    ) {

        message.style.display =
            "none";
    });

}, 5000);

// =======================================
// End of File
// =======================================