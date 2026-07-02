# $NetBSD$

DISTNAME=	fspath-20230629
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=f/fspath/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/return42/fspath
COMMENT=	semantic path names and more
LICENSE=	gnu-gpl-v3

DEPENDS+=	${PYPKGPREFIX}-six>=0:../../lang/py-six

USE_LANGUAGES=	# none

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
