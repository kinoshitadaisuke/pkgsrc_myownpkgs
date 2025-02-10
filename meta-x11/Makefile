# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-x11-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs x11
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for X11 tools and applications
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# graphics
DEPENDS+=	adwaita-icon-theme>=0:../../graphics/adwaita-icon-theme
DEPENDS+=	breeze-icons>=0:../../graphics/breeze-icons
DEPENDS+=	oxygen-icons>=0:../../graphics/oxygen-icons
DEPENDS+=	wm-icons>=0:../../graphics/wm-icons

# time
DEPENDS+=	emiclock>=0:../../time/emiclock
DEPENDS+=	oclock>=0:../../time/oclock
DEPENDS+=	xclock>=0:../../time/xclock

# wm
DEPENDS+=	fvwm3>=0:../../wm/fvwm3

# x11
DEPENDS+=	kde-workspace4>=0:../../x11/kde-workspace4
DEPENDS+=	kterm>=0:../../x11/kterm
DEPENDS+=	xcursor-capitaine>=0:../../x11/xcursor-capitaine
DEPENDS+=	xcursor-core-hr>=0:../../x11/xcursor-core-hr
DEPENDS+=	xcursor-themes>=0:../../x11/xcursor-themes
DEPENDS+=	xcursor-vanilla-dmz>=0:../../x11/xcursor-vanilla-dmz
DEPENDS+=	xdotool>=0:../../x11/xdotool
DEPENDS+=	xsetroot>=0:../../x11/xsetroot
DEPENDS+=	xterm>=0:../../x11/xterm
DEPENDS+=	xtermcontrol>=0:../../x11/xtermcontrol

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
