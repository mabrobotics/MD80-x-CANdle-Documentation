/* Thermal map for the MD200 test plots: temperature over time and phase current, interpolated
   between the measured runs. Shared by inductive_plot.html and dynamometer_plot.html. */

/* matplotlib "inferno" colormap (plotly.js has no built-in inferno) */
var INFERNO = [[0, '#000004'], [0.1, '#160b39'], [0.2, '#420a68'], [0.3, '#6a176e'], [0.4, '#932667'],
	[0.5, '#bc3754'], [0.6, '#dd513a'], [0.7, '#f37819'], [0.8, '#fca50a'], [0.9, '#f6d746'], [1, '#fcffa4']];

/* linear interpolation of one run at time t, null outside the measured time range */
function runAt(run, t)
{
	var ts = run.t, n = ts.length;
	if (t < ts[0] || t > ts[n - 1]) return null;
	var lo = 0, hi = n - 1;
	while (hi - lo > 1)
	{
		var mid = (lo + hi) >> 1;
		if (ts[mid] <= t) lo = mid; else hi = mid;
	}
	if (ts[hi] == ts[lo]) return run.T[lo];
	return run.T[lo] + (run.T[hi] - run.T[lo]) * (t - ts[lo]) / (ts[hi] - ts[lo]);
}

/* runs: [{a: phase current [A], t: [s], T: [C]}] sorted by current
   dt: time step of the map [s], da: current step of the map [A] */
function thermalMapTrace(runs, dt, da, tMax)
{
	var times = [], currents = [], z = [];
	for (var t = 0; t <= tMax + 1e-9; t += dt) times.push(Math.round(t * 100) / 100);
	var aMin = runs[0].a, aMax = runs[runs.length - 1].a;
	for (var a = aMin; a <= aMax + 1e-9; a += da) currents.push(a);

	/* each measured run resampled on the time grid */
	var rows = runs.map(function (run) { return times.map(function (t) { return runAt(run, t); }); });

	currents.forEach(function (a)
	{
		var i = 0;
		while (i < runs.length - 1 && runs[i + 1].a <= a) i++;
		var zr = [];
		if (runs[i].a == a)
			zr = rows[i].slice();
		else
		{
			var w = (a - runs[i].a) / (runs[i + 1].a - runs[i].a);
			times.forEach(function (t, k)
			{
				var lo = rows[i][k], hi = rows[i + 1][k];
				zr.push(lo === null || hi === null ? null : lo + (hi - lo) * w);
			});
		}
		z.push(zr);
	});

	return { type: 'heatmap', x: times, y: currents, z: z, visible: false, name: 'map',
		colorscale: 'Jet', zmin: 25, zmax: 100, zsmooth: false, hoverongaps: false,
		colorbar: { title: { text: '°C', side: 'top' } },
		hovertemplate: '%{x:.1f} s, %{y} A<br>%{z:.1f} °C<extra></extra>' };
}

/* adds the curves / map switch; nCurves: number of curve traces before the map trace */
function addMapSwitch(layout, nCurves, curvesTitle)
{
	var curves = [], map = [];
	for (var k = 0; k < nCurves; k++) { curves.push(true); map.push(false); }
	curves.push(false); map.push(true);
	layout.updatemenus = [{ type: 'buttons', direction: 'right', x: 0, xanchor: 'left', y: 1.12, yanchor: 'top',
		showactive: true, pad: { r: 4, t: 0 },
		buttons: [
			{ label: 'Curves', method: 'update', args: [{ visible: curves },
				{ showlegend: true, 'yaxis.title.text': curvesTitle, 'xaxis.autorange': true, 'yaxis.autorange': true }] },
			{ label: 'Thermal map', method: 'update', args: [{ visible: map },
				{ showlegend: false, 'yaxis.title.text': 'Phase current [A]', 'xaxis.autorange': true, 'yaxis.autorange': true }] }] }];
	layout.margin.t = Math.max(layout.margin.t, 70);
}

/* opens the plot in the map view when the page address contains "map" */
function mapFromUrl(layout)
{
	if (!new URLSearchParams(location.search).has('map')) return;
	var args = layout.updatemenus[0].buttons[1].args;
	Plotly.update('p', args[0], Object.assign({ 'updatemenus[0].active': 1 }, args[1]));
}
