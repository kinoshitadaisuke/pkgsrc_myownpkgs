# $NetBSD$

DISTNAME=	affine-3.0rc1
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_PYPI:=a/affine/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/affine/
COMMENT=	Affine transformation matrices
LICENSE=	modified-bsd

# TODO: Extract dependencies from pyproject.toml

USE_LANGUAGES=	# none

DEPENDS+=	${PYPKGPREFIX}-flit_core>=0:../../devel/py-flit_core
DEPENDS+=	${PYPKGPREFIX}-numpy>=0:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-test>=0:../../devel/py-test
DEPENDS+=	${PYPKGPREFIX}-test-cov>=0:../../devel/py-test-cov
DEPENDS+=	${PYPKGPREFIX}-coveralls>=0:../../devel/py-coveralls

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
