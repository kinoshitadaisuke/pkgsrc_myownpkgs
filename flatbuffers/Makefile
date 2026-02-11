# $NetBSD$

DISTNAME=	25.12.19-2026-02-06-03fffb2
PKGNAME=	${GITHUB_PROJECT}-${DISTNAME}
CATEGORIES=	devel
MASTER_SITES=	${MASTER_SITE_GITHUB:=google/}
GITHUB_PROJECT=	flatbuffers
GITHUB_TAG=	refs/tags/v${DISTNAME}
DIST_SUBDIR=	${GITHUB_PROJECT}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/google/flatbuffers/
COMMENT=	Memory efficient serialization library
LICENSE=	apache-2.0

WRKSRC=		${WRKDIR}/flatbuffers-${DISTNAME}
USE_TOOLS+=	pkg-config
USE_LANGUAGES=	c++

PKGCONFIG_OVERRIDE+=	CMake/flatbuffers.pc.in

.include "../../devel/cmake/build.mk"
.include "../../mk/bsd.pkg.mk"
