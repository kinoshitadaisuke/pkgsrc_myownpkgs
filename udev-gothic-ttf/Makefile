# $NetBSD$

GITHUB_PROJECT=	udev-gothic
GITHUB_RELEASE=	v2.1.0
DISTNAME=	UDEVGothic_${GITHUB_RELEASE}
PKGNAME=	${GITHUB_PROJECT:tl}-ttf-${GITHUB_RELEASE:S/v//}
CATEGORIES=	fonts japanese
MASTER_SITES=	${MASTER_SITE_GITHUB:=yuru7/}
EXTRACT_SUFX=	.zip
DIST_SUBDIR=	${GITHUB_PROJECT}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/yuru7/udev-gothic/
COMMENT=	udev-gothic font is a Japanese font suitable for programming
LICENSE=	ofl-v1.1

USE_LANGUAGES=	# none

WRKSRC=		${WRKDIR}/${DISTNAME}
NO_CONFIGURE=	yes
NO_BUILD=	yes

.include "../../mk/fonts.mk"
.include "../../mk/bsd.pkg.mk"
