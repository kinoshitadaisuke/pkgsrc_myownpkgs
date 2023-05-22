# $NetBSD$

GITHUB_PROJECT=	Firge
DISTNAME=	Firge_v0.2.0
PKGNAME=	${GITHUB_PROJECT:tl}-ttf-${GITHUB_RELEASE:S/v//}
CATEGORIES=	pkgsrc_myownpkgs
MASTER_SITES=	${MASTER_SITE_GITHUB:=yuru7/}
GITHUB_RELEASE=	v0.2.0
EXTRACT_SUFX=	.zip

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/yuru7/Firge/
COMMENT=	Firge font is a Japanese font suitable for programming
LICENSE=	ofl-v1.1

USE_LANGUAGES=	# none

WRKSRC=		${WRKDIR}/${DISTNAME}
NO_CONFIGURE=	yes
NO_BUILD=	yes

.include "../../mk/fonts.mk"
.include "../../mk/bsd.pkg.mk"
