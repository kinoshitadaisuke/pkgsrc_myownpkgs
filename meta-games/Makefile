# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-games-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs games
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for games
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

# games
DEPENDS+=	crimsonfields>=0:../../games/crimsonfields
DEPENDS+=	freeciv-client>=0:../../games/freeciv-client
DEPENDS+=	freeciv-server>=0:../../games/freeciv-server
DEPENDS+=	lbreakout>=0:../../games/lbreakout
DEPENDS+=	lincity>=0:../../games/lincity
#DEPENDS+=	liquidwar>=0:../../games/liquidwar
DEPENDS+=	maelstrom-sdl>=0:../../games/maelstrom-sdl
DEPENDS+=	minami>=0:../../games/minami
DEPENDS+=	powermanga>=0:../../games/powermanga
DEPENDS+=	sl>=0:../../games/sl
DEPENDS+=	wesnoth>=0:../../games/wesnoth
DEPENDS+=	xbill>=0:../../games/xbill
DEPENDS+=	xgalaga>=0:../../games/xgalaga
DEPENDS+=	xjewel>=0:../../games/xjewel
DEPENDS+=	xkobo>=0:../../games/xkobo
DEPENDS+=	xpuyopuyo>=0:../../games/xpuyopuyo
DEPENDS+=	xsoldier>=0:../../games/xsoldier

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
