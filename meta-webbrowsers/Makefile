# $NetBSD$

DISTNAME=	# empty
PKGNAME=	meta-webbrowsers-1.0
PKGREVISION=	0
CATEGORIES=	meta-pkgs www
MASTER_SITES=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
DISTFILES=	# empty

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/kinoshitadaisuke/pkgsrc_myownpkgs
COMMENT=	Meta package for web browsers
LICENSE=	modified-bsd

META_PACKAGE=	yes

.include "../../mk/bsd.prefs.mk"

DEPENDS+=	arcticfox>=0:../../www/arcticfox
DEPENDS+=	badwolf>=0:../../www/badwolf
DEPENDS+=	chromium>=0:../../www/chromium
#DEPENDS+=	firefox>=0:../../www/firefox
#DEPENDS+=	firefox115>=0:../../www/firefox115
DEPENDS+=	firefox128>=0:../../www/firefox128
DEPENDS+=	midori>=0:../../www/midori
DEPENDS+=	palemoon>=0:../../www/palemoon
DEPENDS+=	qutebrowser>=0:../../www/qutebrowser
DEPENDS+=	seamonkey>=0:../../www/seamonkey
DEPENDS+=	vimb>=0:../../www/vimb

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
