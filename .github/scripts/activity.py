"""Render a BRL-styled contribution activity card (last 31 days) as SVG.

Usage:
  GH_TOKEN=... python3 activity.py <username> <out.svg>
  python3 activity.py --sample <out.svg>        # fake data, for previews
"""
import json, os, sys, urllib.request, datetime, random

W, H = 495, 165                      # matches the top-langs card height
BG, ICE, PURPLE, PEARL, SPARK, GRID = "#0d0f14", "#a6dcff", "#9d5cff", "#e7e3db", "#7ff6ff", "#1a1e27"
DAYS = 31


def fetch(user, token):
    q = {"query": 'query($u:String!){user(login:$u){contributionsCollection{contributionCalendar'
                  '{weeks{contributionDays{date contributionCount}}}}}}', "variables": {"u": user}}
    req = urllib.request.Request("https://api.github.com/graphql", json.dumps(q).encode(),
                                 {"Authorization": f"bearer {token}", "Content-Type": "application/json"})
    weeks = json.load(urllib.request.urlopen(req, timeout=60))["data"]["user"][
        "contributionsCollection"]["contributionCalendar"]["weeks"]
    days = [d for w in weeks for d in w["contributionDays"]]
    days.sort(key=lambda d: d["date"])
    return [(d["date"], d["contributionCount"]) for d in days[-DAYS:]]


def sample():
    today = datetime.date.today()
    return [((today - datetime.timedelta(days=DAYS - 1 - i)).isoformat(), random.randint(4, 40))
            for i in range(DAYS)]


def render(days):
    L, R, T, B = 40, 16, 40, 28                       # plot margins
    pw, ph = W - L - R, H - T - B
    top = max(max(c for _, c in days), 1)
    top = ((top + 4) // 5) * 5                        # round axis max up to a multiple of 5
    x = lambda i: L + pw * i / (len(days) - 1)
    y = lambda c: T + ph - ph * c / top
    pts = [(x(i), y(c)) for i, (_, c) in enumerate(days)]
    line = " ".join(f"{a:.1f},{b:.1f}" for a, b in pts)
    area = f"{L},{T + ph} {line} {L + pw},{T + ph}"
    total = sum(c for _, c in days)

    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
         f'role="img" aria-label="Contribution activity, last {DAYS} days: {total} contributions">',
         f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="4.5" fill="{BG}"/>',
         f'<text x="25" y="27" fill="{ICE}" font-family="Segoe UI,Ubuntu,sans-serif" font-size="18" '
         f'font-weight="600">Contribution Activity</text>',
         f'<text x="{W-25}" y="27" fill="{PEARL}" font-family="Segoe UI,Ubuntu,sans-serif" font-size="12" '
         f'text-anchor="end">{total} in the last {DAYS} days</text>']
    for k in range(3):                                # grid lines + y labels at 0, mid, top
        v = top * k / 2
        gy = y(v)
        s.append(f'<line x1="{L}" y1="{gy:.1f}" x2="{L+pw}" y2="{gy:.1f}" stroke="{GRID}"/>')
        s.append(f'<text x="{L-6}" y="{gy+4:.1f}" fill="{PEARL}" font-family="Segoe UI,Ubuntu,sans-serif" '
                 f'font-size="10" text-anchor="end">{int(v)}</text>')
    s.append(f'<polygon points="{area}" fill="{PURPLE}" fill-opacity="0.25"/>')
    s.append(f'<polyline points="{line}" fill="none" stroke="{ICE}" stroke-width="2" stroke-linejoin="round"/>')
    s += [f'<circle cx="{a:.1f}" cy="{b:.1f}" r="2.2" fill="{SPARK}"/>' for a, b in pts]
    for i in (0, len(days) // 2, len(days) - 1):      # x labels: first, middle, last day
        d = datetime.date.fromisoformat(days[i][0])
        s.append(f'<text x="{x(i):.1f}" y="{H-10}" fill="{PEARL}" font-family="Segoe UI,Ubuntu,sans-serif" '
                 f'font-size="10" text-anchor="middle">{d.strftime("%b")} {d.day}</text>')
    s.append("</svg>")
    return "\n".join(s)


if __name__ == "__main__":
    if sys.argv[1] == "--sample":
        days = sample()
    else:
        days = fetch(sys.argv[1], os.environ["GH_TOKEN"])
    with open(sys.argv[2], "w") as f:
        f.write(render(days))
