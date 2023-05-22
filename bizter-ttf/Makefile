# $NetBSD$

GITHUB_PROJECT=	BIZTER
DISTNAME=	BIZTER_v0.0.1
PKGNAME=	${GITHUB_PROJECT:tl}-ttf-${GITHUB_RELEASE:S/v//}
CATEGORIES=	fonts japanese
MASTER_SITES=	${MASTER_SITE_GITHUB:=yuru7/}
GITHUB_RELEASE=	v0.0.1
EXTRACT_SUFX=	.zip

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/yuru7/BIZTER/
COMMENT=	bizter is a Japanese font
LICENSE=	ofl-v1.1

USE_LANGUAGES=	# none

WRKSRC=		${WRKDIR}/${DISTNAME}
NO_CONFIGURE=	yes
NO_BUILD=	yes

.include "../../mk/fonts.mk"
.include "../../mk/bsd.pkg.mk"
