import dash_bootstrap_components as dbc
from dash import html

LOGO = "https://media.user.com/uploads/28svf1-onnibus-com/000930-car-logo-design-free-logos-online-05-removebg-preview_dItah2H.png"

header = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=LOGO, height="50px")),
                        dbc.Col(
                            dbc.NavbarBrand("Dashboard about Cars!", className="ms-2")
                        ),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://dash-bootstrap-components.opensource.faculty.ai/docs/components/navbar/",
                # style={"textDecoration": "none"},
            )
        ]
    ),
    color="dark",
    dark=True,
)


alert = html.Div(
    [
        dbc.Alert(
            "Hello! Cross filtering is implemented between two scatter plot graphs.",
            id="alert-fade",
            dismissable=True,
            is_open=True,
            color="info",
        ),
    ]
)
