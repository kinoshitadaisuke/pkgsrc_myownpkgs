# $NetBSD$

GITHUB_PROJECT=	mint-mono
GITHUB_RELEASE=	v0.0.1
DISTNAME=	${GITHUB_PROJECT:S/mint-mono/MintMono/}_${GITHUB_RELEASE}
PKGNAME=	${GITHUB_PROJECT:S/-//}-ttf-${GITHUB_RELEASE:S/v//}
CATEGORIES=	fonts japanese
MASTER_SITES=	${MASTER_SITE_GITHUB:=yuru7/}
EXTRACT_SUFX=	.zip

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/yuru7/mint-mono/
COMMENT=	MintMono font suitable for programming
LICENSE=	ofl-v1.1

USE_LANGUAGES=	# none

WRKSRC=	${WRKDIR}/${DISTNAME}
NO_CONFIGURE=	yes
NO_BUILD=	yes

.include "../../mk/fonts.mk"
.include "../../mk/bsd.pkg.mk"
