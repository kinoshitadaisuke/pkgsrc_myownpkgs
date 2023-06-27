# $NetBSD$

GITHUB_PROJECT=	Cica
GITHUB_RELEASE=	v5.0.3
DISTNAME=	${GITHUB_PROJECT}_${GITHUB_RELEASE}
PKGNAME=	${GITHUB_PROJECT:tl}-ttf-${GITHUB_RELEASE:S/v//}
CATEGORIES=	fonts japanese
MASTER_SITES=	${MASTER_SITE_GITHUB:=miiton/}
EXTRACT_SUFX=	.zip

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/miiton/Cica/
COMMENT=	Cica font is a Japanese font suitable for programming
LICENSE=	ofl-v1.1

WRKSRC=		${WRKDIR}
USE_LANGUAGES=	# none
NO_CONFIGURE=	yes
NO_BUILD=	yes

.include "../../mk/fonts.mk"
.include "../../mk/bsd.pkg.mk"
