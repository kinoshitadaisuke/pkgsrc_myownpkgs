# $NetBSD$

GITHUB_PROJECT=	pending-mono
GITHUB_RELEASE=	v0.0.2
DISTNAME=	PendingMonoHW_${GITHUB_RELEASE}
PKGNAME=	${GITHUB_PROJECT:S/pending-mono/pendingmono/}-ttf-${GITHUB_RELEASE:S/v//}
CATEGORIES=	fonts
MASTER_SITES=	${MASTER_SITE_GITHUB:=yuru7/}
EXTRACT_SUFX=	.zip
DIST_SUBDIR=	${GITHUB_PROJECT}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/yuru7/pending-mono/
COMMENT=	TTF font suitable for programming
LICENSE=	ofl-v1.1

USE_LANGUAGES=	# none

WRKSRC=		${WRKDIR}/${DISTNAME}
NO_CONFIGURE=	yes
NO_BUILD=	yes

.include "../../mk/fonts.mk"
.include "../../mk/bsd.pkg.mk"
