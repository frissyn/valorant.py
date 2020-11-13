function setTheme(themeName) {
	localStorage.setItem('theme', themeName);

	var link = document.createElement('link');
	link.rel = 'stylesheet';
	if (themeName == "theme-dark") {
		link.href = 'https://cdn.jsdelivr.net/gh/kognise/water.css@latest/dist/dark.min.css';
	} else {
		link.href = 'https://cdn.jsdelivr.net/gh/kognise/water.css@latest/dist/light.min.css';
	}
	document.head.appendChild(link);
}

// function to toggle between light and dark theme
function toggleTheme() {
	if (localStorage.getItem('theme') === 'theme-dark') {
		setTheme('theme-light');
	} else {
		setTheme('theme-dark');
	}
}

// Immediately invoked function to set the theme on initial load
(function () {
	if (localStorage.getItem('theme') === 'theme-light') {
		setTheme('theme-light');
	} else {
		setTheme('theme-dark');
	}
})();