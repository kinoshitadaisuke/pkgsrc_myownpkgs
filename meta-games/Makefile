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
DEPENDS+=	minami>=0:../../games/minami
DEPENDS+=	wesnoth>=0:../../games/wesnoth

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
