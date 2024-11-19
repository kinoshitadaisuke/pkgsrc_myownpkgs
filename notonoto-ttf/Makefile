# $NetBSD$

GITHUB_PROJECT=	NOTONOTO
GITHUB_RELEASE=	v0.0.1
DISTNAME=	${GITHUB_PROJECT}_${GITHUB_RELEASE}
PKGNAME=	${GITHUB_PROJECT:tl}-ttf-${GITHUB_RELEASE:S/v//}
CATEGORIES=	fonts japanese
MASTER_SITES=	${MASTER_SITE_GITHUB:=yuru7/}
EXTRACT_SUFX=	.zip

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/yuru7/NOTONOTO/
COMMENT=	Japanese font using Noto fonts for programming
LICENSE=	ofl-v1.1

USE_LANGUAGES=	# none

WRKSRC=         ${WRKDIR}/${DISTNAME}
NO_CONFIGURE=   yes
NO_BUILD=       yes

.include "../../mk/fonts.mk"
.include "../../mk/bsd.pkg.mk"
