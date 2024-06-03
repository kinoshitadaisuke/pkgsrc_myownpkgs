# $NetBSD$

GITHUB_PROJECT=	moralerspace
GITHUB_RELEASE=	v1.0.0
DISTNAME=	MoralerspaceHWNF_${GITHUB_RELEASE}
PKGNAME=	${GITHUB_PROJECT}-ttf-${GITHUB_RELEASE:S/v//}
CATEGORIES=	fonts japanese
MASTER_SITES=	${MASTER_SITE_GITHUB:=yuru7/}
GITHUB_RELEASE=	v1.0.0
EXTRACT_SUFX=	.zip
DIST_SUBDIR=	${GITHUB_PROJECT}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/yuru7/moralerspace/
COMMENT=	Moralerspace font for programming
LICENSE=	ofl-v1.1

USE_LANGUAGES=	# none

WRKSRC=		${WRKDIR}/${DISTNAME}
NO_CONFIGURE=	yes
NO_BUILD=	yes

.include "../../mk/fonts.mk"
.include "../../mk/bsd.pkg.mk"
